<template>
  <div>
    <div v-if="userStore.user">
      {{ userStore.getUserName  }}

      <a href="#" @click="logOut"> Log out</a>
    </div>
    <div v-else>
      <RouterLink to="login">
        <img src=../static/image/pngwing.com.png height="30" width="30">
      </RouterLink>
    </div>
  </div>
</template>

<script>
import {useUserStore} from "../../stores/user";

export default {
  name: "UserBadge",
  setup() {
    const userStore = useUserStore();
    return {
      userStore
    }
  },
  data() {
    return {
      user: this.userStore.user
    }
  },
  methods: {
    logOut() {
      this.userStore.logOut()
    },
    logIn() {
      this.userStore.logIn()
    }
  }
}
</script>

<style scoped>

</style>