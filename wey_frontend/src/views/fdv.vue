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
.conversation-item, .router-link {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.conversation-item:hover, .router-link:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.message-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.message-content.self-message {
  align-items: flex-end;
}

.message-text {
  margin: 10px;
}
</style>

<style scoped>
.col-span-4 {
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for transform and shadow */
}

.col-span-4:hover {
  transform: scale(1.05); /* Slightly enlarge on hover */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* Increase shadow for depth */
}
</style>

<style scoped>
/* General container styling, assuming it's a flex container */
.col-span-4 {
  display: flex;
  flex-direction: column;
  align-items: center; /* This will center the content horizontally */
  justify-content: center; /* This will center the content vertically */
  text-align: center; /* Centers text for block elements within */
  width: 100%; /* Full width of the parent container or adjust as needed */
  padding: 20px; /* Padding around the container */
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for aesthetic depth */
  border-radius: 8px; /* Rounded corners */
  background-color: #ffffff; /* White background */
}

/* Styling for the heading */
.col-span-4 h2 {
  font-size: 1.5rem; /* Slightly larger text for heading */
  font-weight: bold; /* Bold font weight for heading */
  color: #333; /* Dark color for better readability */
  margin-bottom: 0.5rem; /* Space below the heading */
}

/* Styling for the paragraph */
.col-span-4 p {
  margin-bottom: 1rem; /* Space below the paragraph before the link */
}

/* Styling for the router link - acts as a button */
.router-link {
  display: inline-block; /* Necessary for dimensions and centering */
  background-color: #007bff; /* Primary button color */
  color: white; /* Text color */
  text-decoration: none; /* No underline */
  padding: 10px 20px; /* Padding inside the button */
  border-radius: 0.375rem; /* Rounded corners for the button */
  font-weight: medium; /* Medium font weight for button text */
  transition: background-color 0.3s ease; /* Smooth transition for hover effect */
}

.router-link:hover {
  background-color: #0056b3; /* Darker blue on hover for the button */
}
</style>