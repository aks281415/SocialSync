<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="space-y-4">
                    <div class="flex items-center justify-between" v-for="conversation in conversations"
                        v-bind:key="conversation.id" v-on:click="setActiveConversation(conversation.id)">
                        <div class="flex items-center space-x-2">

                            <div v-for="user in conversation.users" v-bind:key="user.id">
                                <img :src="user.get_avatar" class="w-[40px] rounded-full">

                                <p class="text-xs font-bold" v-if="user.id !== userStore.user.id">{{ user.name }}</p>
                            </div>
                        </div>

                        <span class="text-xs text-gray-500">{{ conversation.modified_at_formatted }} ago</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="flex flex-col flex-grow p-4">
                    <div v-for="message in activeConversation.messages" v-bind:key="message.id">
                        <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                            v-if="message.created_by.id == userStore.user.id">
                            <div>
                                <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                    <p class="text-sm">{{ message.body }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">{{ message.created_at_formatted }}
                                    ago</span>
                            </div>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full">
                            </div>
                        </div>

                        <div class="flex w-full mt-2 space-x-3 max-w-md" v-else>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full">
                            </div>
                            <div>
                                <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                    <p class="text-sm">{{ message.body }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">{{ message.created_at_formatted }}
                                    ago</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-white border border-gray-200 rounded-lg">
                <form @submit.prevent="submitForm" class="p-4 flex items-end"> <!-- Use flex to align items inline -->
                    <textarea v-model="body" class="flex-grow bg-gray-100 rounded-lg p-4 mr-4"
                        placeholder="What do you want to say?" rows="1"></textarea> <!-- Textarea as a flex item -->
                    <button type="submit" class="py-2 px-6 bg-purple-600 text-white rounded-lg">Send</button>
                    <!-- Button as a flex item -->
                </form>
            </div>
            <div class="col-span-4">
            <div class="ai-container p-6 bg-white border border-gray-200 rounded-lg shadow-lg text-center">
                <h2 class="text-2xl font-bold mb-4 text-gray-700">My AI</h2>
                <p class="mb-4 text-gray-600">Your own AI-powered chatbot</p>
                <router-link to="/chatbot" class="btn-primary">Go to Chatbot</router-link>
            </div>
        </div>
        </div>
    </div>

    <!-- New section for AI Chatbot link -->

</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
    name: 'chat',
    setup() {
        const userStore = useUserStore()
        return { userStore }
    },
    data() {
        return {
            conversations: [],
            activeConversation: {},
            body: ''
        }
    },
    mounted() {
        this.getConversations()
    },
    methods: {
        setActiveConversation(id) {
            console.log('setActiveConversation', id)
            this.activeConversation = id
            this.getMessages()
        },
        getConversations() {
            console.log('getConversations')
            axios
                .get('/api/chat/')
                .then(response => {
                    console.log(response.data)
                    this.conversations = response.data
                    if (this.conversations.length) {
                        this.activeConversation = this.conversations[0].id
                    }
                    this.getMessages()
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getMessages() {
            console.log('getMessages')
            axios
                .get(`/api/chat/${this.activeConversation}/`)
                .then(response => {
                    console.log(response.data)
                    this.activeConversation = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        submitForm() {
            console.log('submitForm', this.body)
            axios
                .post(`/api/chat/${this.activeConversation.id}/send/`, {
                    body: this.body
                })
                .then(response => {
                    console.log(response.data)
                    this.activeConversation.messages.push(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>

<style scoped>
/* Styling for the AI container */
.ai-container {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    /* Adds a smooth transition effect for transform and shadow */
}

.ai-container:hover {
    transform: translateY(-5px);
    /* Slightly moves the container up on hover */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    /* Adds a more prominent shadow on hover */
}

/* Styling for the heading in the AI container */
.ai-container h2 {
    font-size: 1.75rem;
    /* Larger font size for heading */
    font-weight: bold;
    /* Bold font weight for heading */
    color: #4a5568;
    /* Slightly darker gray for heading */
}

/* Styling for the paragraph in the AI container */
.ai-container p {
    color: #718096;
    /* Gray color for paragraph */
    margin-bottom: 1rem;
    /* Space below the paragraph */
}

/* Styling for the router link button */
.btn-primary {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    /* Adds padding inside the button */
    background-color: #3182ce;
    /* Blue background color */
    color: white;
    /* White text color */
    border-radius: 0.375rem;
    /* Rounded corners */
    text-decoration: none;
    /* Removes underline from link */
    font-weight: medium;
    /* Medium font weight */
    transition: background-color 0.3s ease;
    /* Smooth transition for background color */
}

.btn-primary:hover {
    background-color: #2b6cb0;
    /* Darker blue on hover */
}

/* Ensures other containers have smooth transitions */
.col-span-4 {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.col-span-4:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
</style>



