<template>
  <div class="chatbot">
    <div class="messages" ref="messages">
      <transition-group name="list" tag="div">
        <div v-for="message in messages" :key="message.id" class="message">
          <div v-if="message.type === 'user'" class="user-message">
            {{ message.content }}
          </div>
          <div v-else class="bot-message">
            {{ message.content }}
          </div>
        </div>
      </transition-group>
    </div>
    <form @submit.prevent="sendMessage" class="chat-form">
      <input v-model="inputMessage" type="text" placeholder="Type your message..." aria-label="Type your message">
      <button type="submit" aria-label="Send message">Send</button>
    </form>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'ChatbotView',
  data() {
    return {
      inputMessage: '',
      messages: [],
      typingTimeout: null // Store timeout to manage intervals
    };
  },
  methods: {
    async sendMessage() {
      if (!this.inputMessage.trim()) return;

      // Add user message to array
      this.messages.push({
        id: Date.now(),
        type: 'user',
        content: this.inputMessage.trim()
      });

      // Clear input field after sending message
      this.inputMessage = '';

      try {
        const response = await axios.post('/api/chatbot/', {
          message: this.messages[this.messages.length - 1].content
        });

        // Prepare to simulate typing effect
        this.simulateTyping(response.data.message);
      } catch (error) {
        console.error('Error sending message:', error);
      }
    },
    simulateTyping(fullMessage) {
      let index = 0;
      let displayedMessage = '';
      const messageId = Date.now();
      this.messages.push({
        id: messageId,
        type: 'bot',
        content: '' // Start with an empty message
      });

      const typingSpeed = 50; // milliseconds per character
      clearInterval(this.typingTimeout); // Clear any previous typing effect
      this.typingTimeout = setInterval(() => {
        if (index < fullMessage.length) {
          displayedMessage += fullMessage.charAt(index++);
          // Update the last message in the array (bot's message) with new content
          this.messages[this.messages.length - 1].content = displayedMessage;
        } else {
          clearInterval(this.typingTimeout);
          // Ensure scrolling happens after the message is fully typed
          this.$nextTick(() => {
            this.$refs.messages.scrollTop = this.$refs.messages.scrollHeight;
          });
        }
      }, typingSpeed);
    }
  }
});
</script>

<style scoped>
.chatbot {
  position: relative;
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background: url('@/assets/chat2.jpeg') no-repeat center center/cover; /* Background image */
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
}

.messages {
  flex-grow: 1;
  overflow-y: auto;
  margin-bottom: 10px;
  padding: 5px;
}

.message {
  display: flex;
  flex-direction: column;
  transition: transform 0.5s ease-in-out;
}

.user-message, .bot-message {
  padding: 10px;
  border-radius: 8px;
  margin: 5px 0;
  max-width: 80%;
}

.user-message {
  background-color: #f0f0f0;
  align-self: flex-end;
}

.bot-message {
  background-color: #e0f7fa;
  align-self: flex-start;
}

form.chat-form {
  display: flex;
  padding: 10px 0;
}

input[type="text"] {
  flex: 1;
  padding: 10px;
  border: 2px solid #ddd;
  border-radius: 4px;
}

input[type="text"]:focus {
  border-color: #007bff;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.list-enter-active, .list-leave-active {
  transition: all 0.5s ease;
}

.list-enter, .list-leave-to {
  transform: translateY(30px);
  opacity: 0;
}
</style>
