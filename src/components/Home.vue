<script setup>
  import { ref } from 'vue';
  import NavBar from './NavBar.vue';
  // const items = ref([1, 2]);

</script>
<template>
  <NavBar/>
  <div class="content-main">
    <h2 class="title px-3">Home</h2>
    <div class="pt-3 px-3 list-img d-flex flex-wrap justify-content-between">
      <div class="v-card d-flex" v-for="n in 5" :key="n">
        <div class="w-80 img-item">
          <div class="h-80 p-2 d-flex align-items-center justify-content-center img-border">
            <div>
              <img :src="`public/images/item${n}.png`" alt="">
            </div>
          </div>
          <div class="h-20 p-2 text-center img-content">
            <div class="img-title">Title</div>
            <div>Description</div>
          </div>
        </div>
        <div class="w-20 img-star">
          <div class="d-flex flex-column justify-content-center h-100">
            <div class="star">
            </div>
            <div class="star">
            </div>
            <!-- // -->
            <div class="mt-auto btn-delete">
              <div class="trash">
                <font-awesome-icon icon="fa-regular fa-trash-can" />
              </div>
            </div>
            
            <!-- <font-awesome-icon icon="fa-solid fa-user-secret" /> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.list-img {
  row-gap: 15px;
  .v-card {
    width: 275px;
    border: 10px solid #eee;
    .img-star {
      .btn-delete {
        width: 35px;
        height: 35px;
        .trash {
          width: 100%;
          height: 100%;
          display: flex;
          justify-content: center;
          align-items: center;
          color: red;
          border-top: 1px solid #eee;
          border-left: 1px solid #eee;
        }
      }
      .star {
        --percent: calc(2.3 / 5 * 100%);
        display: inline-block;
        font-size: 35px;
        font-family: Times;
        line-height: 1;
        &::before {
          content: "★";
          letter-spacing: 3px;
          background: linear-gradient(90deg, #fc0 var(--percent), #F3F4F6 var(--percent));
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
      }
    }

    .img-item {
      height: 100%;
      .img-border {
        border-right: 1px solid #eee;
      }
      .img-content {
        border-top: 1px solid #eee;
        .img-title {
          font-size: 20px;
          font-weight: 600;
        }
      }
    }
  }
  .w-20 {
    width: 35px;
  }
  .w-80 {
    width: calc(100% - 35px);
  }
  .h-20 {
    height: calc(100% - 240px);
  }
  .h-80 {
    height: 240px;
  }
}
</style>

<script>
import axios from 'axios';

export default {
  setup() {
    var dataUser = '';
    if ($cookies.isKey('data_user')) {
      dataUser = $cookies.get('data_user');
    }
    return {
      dataUser
    };
  },
  mounted() {
    if ($cookies.isKey('data_user')) {
      let $dataUser = $cookies.get('data_user');
      let $id = $dataUser.user.id
      axios.get(`/api/user/${$id}/list-image`)
        .then(response => {
          if (response.data.data) {
            console.log(response.data.data);
          }
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>