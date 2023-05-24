<template>
  <!-- <div class="signup-page">
  <div class="container">
    <div class="input-form-backgroud row">
    <h1>회원 가입 페이지</h1>
    <form @submit.prevent="signUp">
      <div class="mb-3">
        <label for="username" class="form-label">사용자명:</label>
        <input type="text" id="username" v-model="username" class="form-control">
      </div>

      <div class="mb-3">
        <label for="password1" class="form-label">비밀번호:</label>
        <input type="password" id="password1" v-model="password1" class="form-control">
      </div>

      <div class="mb-3">
        <label for="password2" class="form-label">비밀번호 확인:</label>
        <input type="password" id="password2" v-model="password2" class="form-control">
      </div>

      <button type="submit" class="btn btn-primary">가입하기</button>
    </form>
  </div>
  </div>
  </div> -->
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
      <div class="col-lg-6 text-center text-lg-start">
        <img class="col-lg-10 img1" src="@/assets/hyungnim.jpg" alt="오태식">
        <h2 class="text-white display-4 fw-bold lh-1 mb-3">회원가입</h2>
        <p class="text-white col-lg-10 fs-4">이건 기회야...</p>
        <p class="text-white col-lg-10 fs-4">회원가입을 해서 형님들에게</p>
        <p class="text-white col-lg-10 fs-4">깊은 인상을 남겨줄거야...</p>
      </div>
      <div class="col-md-10 mx-auto col-lg-6">
        <form class="p-4 p-md-5 border rounded-3 bg-light" @submit.prevent="signUp">
          
          <div class="form-floating mb-3">
            
            <input type="text" id="username" v-model="username" class="form-control">
            <label for="floatingInput">ID</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="password1" type="password" class="form-control" id="floatingPassword" >
            <label for="floatingPassword">비밀번호</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="password2" type="password" class="form-control" id="floatingPassword" >
            <label for="floatingPassword">비밀번호 확인</label>
          </div>
          <!-- <div class="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me"> Remember me
            </label>
          </div> -->
          <button class="w-100 btn btn-lg btn-primary" type="submit">회원가입</button>
          <hr class="my-4">
          <small class="text-muted">희주 얼굴 그렇게 만든 놈 누구냐</small>
          <br>
          <small class="text-muted">양식 다 맞춰서 회원가입해라</small>
        </form>
      </div>
    </div>
  </div>
  </div>
</template>

<script>


export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
    

      const payload = {
        username, password1, password2, 
      }
      // if (this.selectedGenres.length != 3) {
      //   alert('3개의 장르를 선택해야 합니다.')
      //   return;
      // }
      
      this.$store.dispatch('signUp', payload)
    },
    
    // checkGenreLimit(genreId) {
    //   if (this.selectedGenres.length > 3) {
    //     const index = this.selectedGenres.indexOf(genreId);
    //     this.selectedGenres.splice(index, 1); // 이전 상태로 되돌립니다.
    //     const checkbox = event.target;

    //     checkbox.checked = false; // 체크박스의 checked 속성을 조작하여 해제합니다.
    //     alert('3개 이상의 장르를 선택할 수 없습니다.');
    //   }
    // },
  },
  mounted() {
    
  }
  }

</script>

<style>
    .signup-page {
  background-image: url(@/assets/mrsun.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}

    .input-form {
      max-width: 680px;

      margin-top: 80px;
      padding: 32px;

      background: #fff;
      -webkit-border-radius: 10px;
      -moz-border-radius: 10px;
      border-radius: 10px;
      -webkit-box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15);
      -moz-box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15);
      box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15)
    }

</style>