<template>
  <div class="login ">
    <!-- <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form> -->
    <!--  -->
  

  <div class="container col-xl-10 col-xxl-8 px-4 py-5 ">
    <div class="row align-items-center g-lg-5 py-5">
      <div class="col-lg-7 text-center text-lg-start">
        <img class="col-lg-10 img1" src="@/assets/jaesoo.jpg" alt="오태식">
        <h2 class="text-white display-4 fw-bold lh-1 mb-3">로그인</h2>
        <p class="text-white col-lg-10 fs-4">어떤 친구가 재수없게 로그인을 안하고 xx이야!!!!</p>
      </div>
      <div class="col-md-10 mx-auto col-lg-5">
        <form class="p-4 p-md-5 border rounded-3 bg-light" @submit.prevent="login">
          <div class="form-floating mb-3">
            <input v-model="username" type="text" class="form-control" id="floatingInput" placeholder="name">
            <label for="floatingInput">ID</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
            <label for="floatingPassword">Password</label>
          </div>
          <!-- <div class="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me"> Remember me
            </label>
          </div> -->
          <button class="w-100 btn btn-lg btn-primary" type="submit">로그인</button>
          <hr class="my-4">
          <small class="text-muted">태식아 아이디랑 비밀번호를 누르고</small>
          <br>
          <small class="text-muted">로그인 눌러라</small>
        </form>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    }
  }
}
</script>

<style>
.login{
  height:80vh;
}
.img1{
  margin-bottom: 30px;
  width: 80%;
  
}
</style>
