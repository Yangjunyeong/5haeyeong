<template>
  <div>
    <div class="card" style="width: 8rem;">
        <img v-bind:src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="card-img-top" alt="image">
        <div class="card-body">
            <h5 class="card-title">{{ movie.title ? movie.title:movie.name }}</h5>
            <div>
                <p class="card-text overview">{{ movie.overview }}</p>
            </div>
        </div>
    </div>
  </div>
</template>


<script>
export default {
    name:'MovieCard',
    props: {
        movie: Object,
    },
}
</script>


<style>
.overview p{
    width: 500px;
    -webkit-line-clamp: 3;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
</style>