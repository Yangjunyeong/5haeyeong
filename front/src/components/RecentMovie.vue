<template>
  <div class="movie-card">
    <img :src="getImageUrl(movie.poster_path)" :alt="movie.title" class="movie-image">
    <h3 class="movie-title">{{ movie.title }}</h3>
    <!-- <p class="movie-overview">{{ movie.overview }}</p> -->
    <!-- 추가적인 영화 정보나 버튼 등을 추가할 수 있습니다 -->
  </div>
</template>

<script>
export default {
  name: 'RecentMovie',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  methods: {
    getImageUrl(posterPath) {
      // 포스터 이미지 경로를 완성하는 메서드
      if (posterPath) {
        return `https://image.tmdb.org/t/p/w500${posterPath}`;
      }
      // 포스터 이미지가 없을 경우 대체 이미지를 사용하거나 기타 처리를 할 수 있습니다.
      return require('@/assets/poster.png'); // placeholder.png 파일 경로에 맞게 수정
    },
  },
};
</script>

<style scoped>
.movie-card {
  background-color: #f7f7f7;
  border-radius: 8px;
  padding: 0;
  text-align: center;
  height: 200px;
  width:  160px;
  margin-left: 10px;
}

.movie-image {
  width: 100%;
  /* max-height: 300px; */
  object-fit: cover;
  border-radius: 8px;
}

.movie-title {
  font-size: 18px;
  font-weight: bold;
  margin-top: 10px;
}

.movie-overview {
  margin-top: 10px;
}
</style>