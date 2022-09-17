<template>
  <form>
    <div class="mb-3 row">
      <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="staticEmail" v-model="data.email">
        {{ error.email }}
      </div>
    </div>
    <div class="mb-3 row">
      <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="inputPassword" v-model="data.password">
        {{ error.password }}
      </div>
    </div>
    <div class="header">
      <a class="lins" href="/register">Register</a>
      <a class="lins" href="#">Forgot Password!?</a>
      <button type="submit" class="btn btn-primary">Log in</button>
    </div>
    <div class="socity">
      <h4>
        or use social media
      </h4>
    </div>
    <div class="cocity">
      <img src=../static/image/pngwing.com.png height="30" width="30">
      <button type="button" class="button button--large button--gray button--with-icon auth-modal__social-button">
        <svg width="18" height="18">
          <use href="icon-google-colored">
          </use>
        </svg>
        Google
      </button>
      <button type="button" class="button button--large button--gray button--with-icon auth-modal__social-button">
        <svg width="18" height="18">
          <use href="icon-google-colored">
          </use>
        </svg>
        Twitter
      </button>
    </div>
  </form>
</template>

<script>
import {useUserStore} from "../stores/user";
import {apiFetch} from "../utils/api"

export default {
  name: "LoginForm",
  data() {
    return {
      data: {
        email: '',
        password: ''
      },
      error: {}
    }
  },
  methods: {
    async loginUser(e) {
      e.preventDefault()
      e.stopPropagation()


      const resp = await apiFetch('/api/v1/auth/token/',
          {
            method: 'POST',
            body: JSON.stringify(this.data)
          }
      )

      if (resp.status !== 200) {
        this.error = await resp.json()
        return
      } else {
        const data = await resp.json()
        localStorage.setItem('userToken', data.access)
        await useUserStore().fetchUser();
        location.href = '/';
      }
    }
  }
}
</script>

<style scoped>
form {
  position: fixed;
  top: 40%;
  left: 40%;
  width: 420px;
}

.header {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  margin-left: 5px;
}

.header a {
  display: inline-block;
  padding: 10px;
}

.mb-3 {
  margin-right: 10px;
}
.cocity{
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}
.cocity img{
  display: inline-block;
  padding: 10px;
}
</style>