<template>
<div>
    <h2>Create Movie</h2>
    <form @submit.prevent="createMovie">
    <div>
        <label>Title:</label>
        <input type="text" v-model="formData.title" required>
    </div>
    <div>
        <label>Release Date:</label>
        <input type="date" v-model="formData.release_date" required>
    </div>
    <div>
        <label>Vote Average:</label>
        <input type="number" v-model="formData.vote_average" required>
    </div>
    <div>
        <label>Genres:</label>
        <input type="text" v-model="formData.genres" required>
    </div>
    <div>
        <label>Overview:</label>
        <textarea v-model="formData.overview" required></textarea>
    </div>
    <div>
        <label>Poster Path:</label>
        <input type="text" v-model="formData.poster_path" required>
    </div>
    <div>
        <label>YouTube Key:</label>
        <input type="text" v-model="formData.youtube_key" required>
    </div>
    <div>
        <label>Actors:</label>
        <input type="text" v-model="formData.actors" required>
    </div>
    <button type="submit">Create</button>
    </form>
</div>
</template>

<script>
import axios from 'axios';

export default {
data() {
    return {
    formData: {
        title: '',
        release_date: '',
        vote_average: null,
        genres: '',
        overview: '',
        poster_path: '',
        youtube_key: '',
        actors: ''
    }
    };
},
methods: {
    createMovie() {
    axios.post('http://127.0.0.1:8000/api/v1/movies/', this.formData)
        .then(response => {
        console.log('Movie created:', response.data);
        // 새로운 영화가 생성된 후의 동작을 수행합니다.
        })
        .catch(error => {
        console.error('Failed to create movie:', error.response.data);
        // 새로운 영화 생성이 실패한 경우의 처리를 수행합니다.
        });
    }
}
}
</script>
