<template>
  <div>
    <section class="d-grid gap-2 col-4 mx-auto">
      <button class="btn btn-primary" @click="randomPick">PICK</button>
    </section>
    <div v-if="randomValue" class="mt-3">
      <div class="d-grid gap-2 col-4 mx-auto" v-if="randomValue">
        <img class="img-fluid" :src="`https://image.tmdb.org/t/p/original${randomValue.poster_path}`" alt="Movie poster">
        <div class="card-body">
          <h5 class="text-center">{{ randomValue.title ? randomValue.title:randomValue.name }}</h5>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
import _ from 'lodash'
export default {
    name:'RandomView',
    data(){
      return{
        randomValue:null
      }
    },
    methods: {
    randomPick() {
      const selectedGenres = this.$store.state.selectedGenres;
      const movies = this.$store.state.Movies;

      // 선택한 장르와 일치하는 영화들을 필터링합니다.
      const matchedMovies = movies.filter(movie => selectedGenres.includes(movie.genre));

      // 일치하는 영화 중에서 랜덤으로 하나를 추출합니다.
      const randomMovie = _.sample(matchedMovies);

      if (randomMovie) {
        const { title, poster_path } = randomMovie;
        this.randomValue = { title, poster_path };
      } else {
        this.randomValue = null;
      }
    },
  },
    created(){
      this.$store.dispatch('getCard')
    }
}
</script>

<style>
.card-body {
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.06);
}
</style>
<!-- Math.floor(Math.random() * 20) -->