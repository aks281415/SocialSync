<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-8 p-4">
        <div class="col-span-3 space-y-6">
            <div class="bg-white border border-gray-300 rounded-lg shadow">
                <form @submit.prevent="submitForm" class="flex flex-col" enctype="multipart/form-data">
                    <textarea v-model="body" class="resize-none p-4 w-full h-40 bg-gray-100 rounded-t-lg border-b"
                              placeholder="What are you thinking about?"></textarea>
                    <div class="flex justify-between items-center p-4">
                        <a href="#" @click.prevent="triggerFileInput" class="inline-flex items-center justify-center py-2 px-4 bg-gray-600 text-white rounded-lg hover:bg-gray-700">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mr-2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6"/>
                            </svg>
                            Attach image
                        </a>
                        <input type="file" ref="fileInput" @change="handleFileChange" class="hidden" />
                        <button type="submit" class="py-2 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-700">Post</button>
                    </div>
                    <div v-if="previewImage" class="p-4">
                        <img :src="previewImage" alt="Image preview" class="w-full h-auto rounded-lg border" />
                    </div>
                </form>
            </div>

            <div v-for="post in posts" :key="post.id" class="p-4 bg-white border border-gray-300 rounded-lg shadow">
                <FeedItem :post="post" />
            </div>
        </div>

        <div class="col-span-1 space-y-6">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>




<script>
import axios from 'axios';
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';
import Trends from '@/components/Trends.vue';
import FeedItem from '@/components/FeedItem.vue';

export default {
    name: 'FeedView',
    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem
    },
    data() {
        return {
            posts: [],
            body: '',
            selectedFile: null,
            previewImage: null
        };
    },
    mounted() {
        this.getFeed();
    },
    methods: {
        getFeed() {
            axios.get('/api/posts/').then(response => {
                this.posts = response.data;
            }).catch(error => console.error(error));
        },
        submitForm() {
            const formData = new FormData();
            formData.append('body', this.body);
            if (this.selectedFile) {
                formData.append('image', this.selectedFile);
            }

            axios.post('/api/posts/create/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(response => {
                this.posts.unshift(response.data);
                this.body = ''; // Clear textarea after posting
                this.selectedFile = null; // Clear file input
                this.previewImage = null; // Clear image preview
            }).catch(error => console.error(error));
        },
        triggerFileInput() {
            this.$refs.fileInput.click();
        },
        handleFileChange(event) {
            const file = event.target.files[0];
            if (file) {
                this.selectedFile = file;
                this.previewImage = URL.createObjectURL(file);
            }
        }
    }
}
</script>



<style scoped>
/* Global font and background setup */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f4f4f8;
}

/* General padding and margin tweaks for cleaner layout */
p, h1, h2, h3, h4, h5, h6, form, button {
    margin: 0;
    padding: 8px;
}

/* Enhancing text area and button interaction */
textarea, button, a {
    transition: all 0.3s ease;
    outline: none;
}

textarea:focus, button:focus, a:focus {
    box-shadow: 0 0 0 2px #805ad5;
}

/* Hover effects for interactive elements */
button:hover, a:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Styling specific for feed items and side components */
.FeedItem, .PeopleYouMayKnow, .Trends {
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
</style>

<style scoped>
/* Preview image styling */
img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    border: 1px solid #ddd;
    margin-top: 10px;
}

/* Additional styling for form and interactive elements */
textarea, button, a {
    transition: all 0.3s ease;
    outline: none;
}

textarea:focus, button:focus, a:focus {
    box-shadow: 0 0 0 2px #805ad5;
}

button:hover, a:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.FeedItem, .PeopleYouMayKnow, .Trends {
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
</style>

