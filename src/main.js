import { createApp } from 'vue';
import './style.css';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle';

import $ from 'jquery';


import App from './App.vue';
import router from './router';
import axios from 'axios';
import VueCookies from 'vue-cookies';
import FontAwesomeIcon from "./font-awesome/font-awesome-icons";

const app = createApp(App);
app.use(router);
app.config.globalProperties.$cookies = VueCookies;
$cookies.config('7d');
app.config.globalProperties.$ = $; 

// Laravel echo
import Echo from 'laravel-echo';
import Pusher from 'pusher-js';

window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'pusher',
    key: 'ccb698dfd5a471dd8c8b',
    cluster: 'ap1',
    encrypted: true,
});

// axios
axios.defaults.baseURL = 'http://service.loc:8888/';
app.config.globalProperties.$axios = axios;

app.component("font-awesome-icon", FontAwesomeIcon);

app.mount('#app');
