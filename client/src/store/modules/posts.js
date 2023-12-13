import { defineStore } from 'pinia';
import { postsService } from '@/api'; 

export const usePostsStore = defineStore('postsStore', {
  state: () => ({
    posts: [],
    specific_post: {},
    cart: [],
  }),
  getters: {
    all_posts: (state) => state.posts,
    post: (state) => state.specific_post,
    shopping_cart: (state) => state.cart,
  },
  actions: {
    async createPost(postData) {
      try {
        const response = await postsService.post('/create_post', postData);
        if (response.status === 201) {
          this.getPosts();
          return "Success"
        } else {
          return response.data.message
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
    async getUserPosts(userId) {
      try {
        const response = await postsService.post('/get_user_posts', { userId: userId });

        if (response.status === 200) {
          this.posts = response.data;
        } else {
          console.error('Failed to get user posts:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching user posts:', error);
      }
    },
    async deleteUserPost(postId) {
      try {
        const response = await postsService.post('/delete_user_post', { post_id: postId });

        if (response.status === 200) {
          return 'User post deleted successfully';
        } else {
          console.error('Failed to delete user post:', response.statusText);
        }
      } catch (error) {
        console.error('Error deleting user post:', error);
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
    async addToCart(postId, quantity = 1) {
      try {
        const response = await postsService.post('/add_to_cart', { post_id: postId, quantity });

        if (response.status === 201) {
          this.getCart();
          return 'Product added to the cart successfully';
        } else {
          console.error('Failed to add product to the cart:', response.statusText);
        }
      } catch (error) {
        console.error('Error adding product to the cart:', error);
      }
    },

    async getCart() {
      try {
        const response = await postsService.post('/get_cart');

        if (response.status === 200) {
          this.cart = response.data;
        } else {
          console.error('Failed to get shopping cart:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching shopping cart:', error);
      }
    },
    async updateQuantity(postId, quantity) {
      try {
        const response = await postsService.post('/update_quantity', { post_id: postId, quantity });

        if (response.status === 200) {
          return 'Quantity updated successfully';
        } else {
          console.error('Failed to update quantity:', response.statusText);
        }
      } catch (error) {
        console.error('Error updating quantity:', error);
      }
    },
    async deleteProduct(postId) {
      try {
        const response = await postsService.post('/delete_product', { post_id: postId });

        if (response.status === 200) {
          return 'Product deleted successfully';
        } else {
          console.error('Failed to delete product:', response.statusText);
        }
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    },
    async deleteAllProducts() {
      try {
        const response = await postsService.post('/delete_all_products');

        if (response.status === 200) {
          return 'All items deleted from cart successfully';
        } else {
          console.error('Failed to delete all items:', response.statusText);
        }
      } catch (error) {
        console.error('Error deleting all items:', error);
      }
    },
    async addComplaint(complaintData) {
      try {
        const response = await postsService.post('/add_complaint', complaintData);
  
        if (response.status === 201) {
          return 'Complaint added successfully';
        } else {
          console.error('Failed to add complaint:', response.statusText);
        }
      } catch (error) {
        console.error('Error adding complaint:', error);
      }
    },
  },
});
