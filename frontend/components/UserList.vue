<template>
    <div class="p-4">
      <h2 class="text-2xl mb-4">Список пользователей</h2>
      
      <table class="min-w-full table-auto mb-4">
        <thead>
          <tr class="bg-gray-200">
            <th class="px-4 py-2">Имя</th>
            <th class="px-4 py-2">Email</th>
            <th class="px-4 py-2">Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id ?? user.name" class="border-b">
            <td class="px-4 py-2">{{ user.name }}</td>
            <td class="px-4 py-2">{{ user.email }}</td>
            <td class="px-4 py-2">
              <button @click="openEditModal(user)" class="bg-blue-500 text-white px-2 py-1 rounded">Редактировать</button>
              <button @click="openDeleteModal(user)" v-if="user.id !== null" class="bg-red-500 text-white px-2 py-1 rounded ml-2">Удалить</button>
            </td>
          </tr>
        </tbody>
      </table>
      
      <button @click="openAddModal" class="bg-green-500 text-white px-4 py-2 mt-4 rounded">Добавить пользователя</button>
  
      <Modal :visible="showModal" @update:visible="showModal = $event">
        <UserForm :initialUser="formData" :isEditing="isEditing" @submitForm="handleEditSubmit" @cancelForm="closeModal" />
      </Modal>
      
      <Modal :visible="showDeleteModal" @update:visible="showDeleteModal = $event">
        <div class="p-4">
          <h3 class="text-xl mb-4">Удалить пользователя</h3>
          <p>Вы уверены, что хотите удалить пользователя {{ formData.name }}?</p>
          <div class="flex justify-end">
            <button @click="confirmDelete" class="bg-red-500 text-white px-4 py-2 rounded">Удалить</button>
            <button @click="closeDeleteModal" class="bg-gray-500 text-white px-4 py-2 ml-2 rounded">Отмена</button>
          </div>
        </div>
      </Modal>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref, reactive, onMounted } from 'vue';
  import axios from 'axios';
  import UserForm from './UserForm.vue';
  import Modal from './Modal.vue';
  
  interface User {
    id: number | null;
    name: string;
    email: string;
  }
  
  const users = ref<User[]>([]);
  const showModal = ref(false);
  const showDeleteModal = ref(false);
  const isEditing = ref(false);
  const formData = reactive<User>({ id: null, name: '', email: '' });
  
  const fetchUsers = async () => {
    const response = await axios.get('/api/users');
    users.value = response.data;
  };
  
  const openAddModal = () => {
    formData.id = null;
    formData.name = '';
    formData.email = '';
    showModal.value = true;
    isEditing.value = false;
  };
  
  const openEditModal = (user: User) => {
    formData.id = user.id;
    formData.name = user.name;
    formData.email = user.email;
    showModal.value = true;
    isEditing.value = true;
  };
  
  const handleEditSubmit = async (formData: User) => {
    if (isEditing.value) {
      if (formData.id !== null) {
        await axios.put(`/api/users/${formData.id}`, formData);
      }
    } else {
      await axios.post('/api/users', formData);
    }
    closeModal();
    fetchUsers();
  };
  
  const closeModal = () => {
    showModal.value = false;
  };
  
  const openDeleteModal = (user: User) => {
    formData.id = user.id;
    formData.name = user.name;
    showDeleteModal.value = true;
  };
  
  const confirmDelete = async () => {
    if (formData.id !== null) {
      await axios.delete(`/api/users/${formData.id}`);
      closeDeleteModal();
      fetchUsers();
    }
  };
  
  const closeDeleteModal = () => {
    showDeleteModal.value = false;
  };
  
  onMounted(() => {
    fetchUsers();
  });
  </script>
  
  <style scoped>
  </style>
  