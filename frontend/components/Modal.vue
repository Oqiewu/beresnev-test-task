<template>
    <div v-if="visible" class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50 z-50">
      <div class="bg-white p-4 rounded shadow-lg">
        <slot></slot>
        <button @click="close" class="mt-4 bg-red-500 text-white px-4 py-2 rounded">Закрыть</button>
      </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue';
  
  const props = defineProps({
    visible: {
      type: Boolean,
      required: true
    }
  });
  
  const emit = defineEmits(['update:visible']);
  
  const close = () => {
    emit('update:visible', false);
  };
  </script>
  
  <style scoped>
  </style>
  