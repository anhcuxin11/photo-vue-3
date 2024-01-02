<template>
  <div class="header">
    <div class="content">
      <div class="nav-bar d-flex align-items-center">
        <div><img :src="`public/images/avatar1.png`" width="80" height="80" class="avatar" alt=""></div>
        <div class="ps-3 text-white">Website to evaluate image quality</div>
        <div class="ms-auto">
          <span v-if="isLogged" class="text-white">{{ dataUser.user.name }}<img class="p-2 logout" :src="`public/images/icon-login-white.svg`" alt="" @click="logout()"></span>
          <router-link to="/login" v-else class="img-login">Login
            <img class="p-2" :src="`public/images/icon-login-grow.svg`" alt="">
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <div class="nav" style="background-color: black;">
    <div class="content d-flex align-items-center">
      <router-link to="/" class="nav-item">Home
      </router-link>
      <router-link to="/notification" class="nav-item">
        <div class="relative">
          <span>Notification</span>
          <span class="notice">3</span>
        </div>
      </router-link>
      <router-link to="/chat" class="nav-item">
        <div class="relative">
          <span>Chat</span>
          <!-- <span class="notice">3</span> -->
        </div>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .header {
    background-color: #434D56;
    position: fixed;
    width: 100%;
  }
  .nav {
    margin-top: 100px;
    background-color: #434D56;
    position: fixed;
    width: 100%;
    .nav-item {
      padding: 7px 15px;
      color: white !important;
      border-left: 2px solid white;
      font-size: 20px;
      &:last-child {
        border-right: 2px solid white;  
      }
    }
    .relative {
      position: relative;
      display: flex;
      align-items: center;
      column-gap: 6px;
    }
    .notice {
      color: white;
      height: 25px;
      width: 25px;
      border-radius: 999em;
      background-color: orange;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 14px;
    }
  }
  .text-white {
    color: white !important;
  }
  .nav-bar {
    height: 100px;
    padding: 10px;
    .logout {
      cursor: pointer;
    }
    .avatar {
      border-radius: 50%;
    }
    .img-login {
      padding: 10px 30px;
      background-color: white;
      border-radius: 999em;
      color: black;
      text-decoration: none;
    }
  }
</style>

<script>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const isLogged = ref(false);
    var dataUser = '';
    if ($cookies.isKey('data_user')) {
      dataUser = $cookies.get('data_user');
    }

    function checkLoginStatus() {
      isLogged.value = $cookies.isKey('data_user');
    }

    watch(isLogged, (newValue, oldValue) => {
      console.log('isLogged changed:', newValue, oldValue);
    });

    function logout() {
        $cookies.remove('data_user');
        isLogged.value = !isLogged.value;
    }

    checkLoginStatus();

    return {
      dataUser,
      isLogged,
      logout
    };
  }
}
</script>

