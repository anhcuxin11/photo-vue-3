<template>
  <div class="content p-top">
    <form class="v-register" @submit.prevent="register">
      <div class="form-group v-name">
        <label for="name">Name:&nbsp;</label> 
        <input type="text" id="name" class="form-control" v-model="name">
      </div>
      <div class="form-group v-email">
        <label for="email">Email:&nbsp;</label> 
        <input type="text" id="email" class="form-control" v-model="email">
      </div>
      <div class="form-group v-password">
        <label for="password">Password:&nbsp;</label> 
        <input type="password" id="password" class="form-control" v-model="password">
      </div>
      <div class="form-group v-password-confirmation">
        <label for="password-confirmation">Password confirm:&nbsp;</label> 
        <input type="password" id="password-confirmation" class="form-control" v-model="passwordConfirmation">
      </div>
      <div class="d-flex justify-content-between align-items-end">
        <div>
          <router-link to="/login">Login</router-link>
        </div>
        <div class="register-submit">
          <button type="submit" class="btn btn-success">Submit</button>
        </div>
      </div>
    </form>
  </div>
</template>

<style lang="scss" scoped>
.p-top {
  padding-top: 200px;
}
.v-register {
  padding: 10px 20px;
  background-color: white;
  border-radius: 6px;
  text-align: left;
  width: 300px;
  margin: 0 auto;
  .v-email {
    padding-bottom: 5px;
  }
  .register-submit {
    margin-top: 12px;
  }
}
</style>
<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const name = ref('');
    const email = ref('');
    const password = ref('');
    const passwordConfirmation = ref('');
    const router = useRouter();

    const register = () => {
      const credentials = {
        name: name.value,
        email: email.value,
        password: password.value,
        password_confirmation: passwordConfirmation.value,
      };

      axios.post('/api/register', credentials)
        .then(response => {
          if (response.data.data.status) {
            // $cookies.set('token', response.data.data.authorization.token, '6h', null, null, true);
            $cookies.set('data_user', response.data.data, '6h', null, null, true);
            router.push('/');
          }
        })
        .catch(error => {
          console.error(error);
        });
    };

    return {
      name,
      email,
      password,
      passwordConfirmation,
      register,
    };
  },
};
</script>