<template>
  <div class="p-4">
    <h2 class="text-2xl mb-4">{{ isEditing ? 'Редактировать' : 'Добавить' }} пользователя</h2>
    <form @submit.prevent="submitForm">
      <div class="mb-4">
        <label for="name" class="block text-gray-700">Имя</label>
        <input type="text" v-model="form.name" id="name" class="border p-2 rounded w-full" required />
      </div>
      <div class="mb-4">
        <label for="email" class="block text-gray-700">Email</label>
        <input type="email" v-model="form.email" id="email" class="border p-2 rounded w-full" required />
      </div>
      <div class="flex justify-end">
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">{{ isEditing ? 'Сохранить' : 'Добавить' }}</button>
        <button type="button" @click="cancelForm" class="bg-gray-500 text-white px-4 py-2 ml-2 rounded">Отмена</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { reactive, watch, defineProps, defineEmits } from 'vue';
import { PropType } from 'vue';

const props = defineProps({
  initialUser: {
    type: Object as PropType<{ id: number | null, name: string, email: string }>,
    required: true
  },
  isEditing: {
    type: Boolean,
    required: true
  }
});

const emit = defineEmits(['submitForm', 'cancelForm']);

const form = reactive<{ id: number | null, name: string, email: string }>({
  id: null,
  name: '',
  email: ''
});

watch(
  () => props.initialUser,
  (newUser) => {
    if (newUser) {
      form.id = newUser.id ?? null;
      form.name = newUser.name ?? '';
      form.email = newUser.email ?? '';
    }
  },
  { immediate: true }
);

const submitForm = () => {
  emit('submitForm', form);
};

const cancelForm = () => {
  emit('cancelForm');
};
</script>
