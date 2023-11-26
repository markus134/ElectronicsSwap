import { defineStore } from 'pinia';
import { postsService } from '@/api'; 

export const usePostsStore = defineStore('postsStore', {
  state: () => ({
    posts: [],
    specific_post: {},
  }),
  getters: {
    all_posts: (state) => state.posts,
    post: (state) => state.specific_post,
  },
  actions: {
    async createPost(postData) {
      try {
        const response = await postsService.post('/create_post', postData);
        if (response.status === 201) {
          // Optionally update state or trigger other actions after creating a post
          this.getPosts();
        } else {
          console.error('Failed to create post:', response.statusText);
        }
      } catch (error) {
        console.error('Error creating post:', error);
      }
    },
    async getPosts() {
      try {
        const response = await postsService.get('/get_posts');
        if (response.status === 200) {
          this.posts = response.data;
        } else {
          console.error('Failed to get posts:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    },
    async getPost(postId) {
        try {
          const response = await postsService.post('/get_post', { postId });

          if (response.status === 200) {
           
            this.specific_post = response.data;
            
          } else {
            console.error('Failed to get post:', response.statusText);
          }
        } catch (error) {
          console.error('Error fetching post:', error);
        }
      },
  },
});
