<template>
  <div>
    <div class="container d-flex">
        <div class="row justify-content-center">
        <MovieCard class="mb-5 col-xs-12 col-md-6 col-lg-4 col-xl-3"
        v-for="movie in movies" :key="movie.id" 
        :movie="movie"
        />
        </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
    name:'MoviesView',
    components:{
        MovieCard,
    },
    created(){
      this.$store.dispatch('getCard')
    },
    computed:{
      movies(){
        return this.$store.state.Movies
      },
      sortedMovies(){
        console.log(this.movies)
        return this.$store.getters.sortedMovies
      }
    }
    }

</script>

<style>

</style>
