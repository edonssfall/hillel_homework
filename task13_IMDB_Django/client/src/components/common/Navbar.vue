<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Movies</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Persons</a>
          </li>
        </ul>
        <UserBadge />
      </div>
    </div>
  </nav>
</template>

<script>
import UserBadge from "./UserBadge.vue";
export default {
  name: "Navbar",
  components: {UserBadge}
}
</script>

<style scoped>
</style>