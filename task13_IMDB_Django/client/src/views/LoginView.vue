<script setup>
import LoginForm from "../components/LoginForm.vue";
import {useUserStore} from "../stores/user";
import {onBeforeMount} from "vue";

const userStore = useUserStore();

onBeforeMount( () =>
{
  if (userStore.getUserId) {
    location.href = '/';
  }
})

</script>

<template>
  <main>
    <LoginForm />
  </main>
</template>