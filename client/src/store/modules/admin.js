import { defineStore } from 'pinia';
import { adminService } from '@/api';  // Import adminService from your API

export const useAdminStore = defineStore('adminStore', {
  state: () => ({
    all_users: [],
    complaints: [],
  }),
  getters: {
    allUsers: (state) => state.all_users,
    allComplaints: (state) => state.complaints,
  },
  actions: {
    async getAllUsers() {
      try {
        const response = await adminService.get('/get_all_users');
        if (response.status === 200) {
          this.all_users = response.data;
        }
      } catch (error) {
        console.error('Failed to get all users:', error);
      }
    },
    async getComplaints() {
      try {
        const response = await adminService.get('/get_all_complaints');
  
        if (response.status === 200) {
          this.complaints = response.data;
        } else {
          console.error('Failed to get complaints:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching complaints:', error);
      }
    },
    async changeRoleToAdmin(target_user_id) {
      const response = await adminService.post('/change_to_admin', { target_user_id: target_user_id })

      if (response.status === 200) {
        return "Success"
      } else {
        return "Fail"
      }
    },
    async demoteToUser(target_user_id) {
      try {
        const response = await adminService.post('/demote_to_user', { target_user_id: target_user_id });

        if (response.status === 200) {
          return "Success";
        } else {
          return "Fail";
        }
      } catch (error) {
        console.error('Error demoting to user:', error);
        return "Fail";
      }
    },
    async banUser(targetUserId, timeExpiry = null) {
      try {
        const response = await adminService.post('/ban_user', {
          target_user_id: targetUserId,
          time_expiry: timeExpiry,
        });

        if (response.status === 200) {
          return "User banned successfully";
        } else {
          return "Failed to ban user";
        }
      } catch (error) {
        console.error('Error banning user:', error);
        return "An error occurred while trying to ban the user";
      }
    },
    async unbanUser(targetUserId) {
      try {
        const response = await adminService.post('/unban_user', {
          target_user_id: targetUserId,
        });

        if (response.status === 200) {
          return "User unbanned successfully";
        } else {
          return "Failed to unban user";
        }
      } catch (error) {
        console.error('Error unbanning user:', error);
        return "An error occurred while trying to unban the user";
      }
    },
    async deleteComplaint(complaintId) {
      try {
        const response = await adminService.post('/delete_complaint', { complaint_id: complaintId });

        if (response.status === 200) {
          // Remove the deleted complaint from the local state
          this.complaints = this.complaints.filter(complaint => complaint.id !== complaintId);
          return "Complaint deleted successfully";
        } else {
          return "Failed to delete complaint";
        }
      } catch (error) {
        console.error('Error deleting complaint:', error);
        return "An error occurred while trying to delete the complaint";
      }
    },
  },
});
