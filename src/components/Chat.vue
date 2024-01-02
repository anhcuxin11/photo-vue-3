<script setup>
  import { ref } from 'vue';
  import NavBar from './NavBar.vue';
  // const items = ref([1, 2]);

</script>
<template>
  <NavBar/>
  <div class="content-main">
    <h2 class="title px-3">Chat</h2>
    <div class="pt-4 px-5">
      <div class="chat-overview">
        <div class="label">Name</div>
        <div class="content"></div>
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
.chat-overview {
  border: 1px solid #eee;
  border-radius: 4px;
  min-height: 300px;
  .label {
    padding: 8px;
    border-bottom: 1px solid #eee;
  }
}
</style>

<script>
import axios from 'axios';

export default {
  setup() {
    const name = ref('');
    const email = ref('');
    const description = ref('');

    return {
      name,
      email,
      description,
    };
  },
  mounted() {
    this.listenForChanges();
    // if ("geolocation" in navigator) {
    //   navigator.geolocation.getCurrentPosition(function(position) {
    //     const latitude = position.coords.latitude;
    //     const longitude = position.coords.longitude;
        
    //     console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
    //   });
    // } else {
    //   console.log("Trình duyệt không hỗ trợ Geolocation.");
    // }
  },
  methods: {
    addMessage() {
      const credentials = {
        name: this.name,
        email: this.email,
        description: this.description,
      };

      axios.post('/api/message', credentials)
        .then(res => {
          if(res.data) {
            console.log(res.data);
          }
        })
        .catch(error => {
          console.error(error);
        });
    },

    listenForChanges() {
      Echo.channel('contact-form')
      .listen('MessagePublished', post => {
        if (! ('Notification' in window)) {
          alert('Web Notification is not supported');
          return;
        }

        Notification.requestPermission( permission => {
          let notification = new Notification('Awesome Website', {
            body: post.message,
            icon: "https://pusher.com/static/pusher-logo-0576fd4af5c38706f96f632235f3124a.svg" // optional image url
          });

          // link to page on clicking the notification
          notification.onclick = () => {
            window.open(window.location.href);
          };
        });
      })
    }
  }
};
</script>