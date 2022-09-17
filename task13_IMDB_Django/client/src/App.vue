<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from "./components/common/Navbar.vue"
import {onMounted} from "vue"
import { useUserStore} from "./stores/user";

const userStore = useUserStore()
onMounted(
    async () => {
      await userStore.fetchUser()
    }
)
</script>

<template>
  <header>
    <Navbar />
  </header>
  <RouterView />
</template>

<style scoped>

</style>
