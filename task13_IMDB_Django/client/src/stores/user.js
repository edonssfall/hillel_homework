import {defineStore} from 'pinia'
import {apiFetch} from "../utils/api";

export const useUserStore = defineStore('user', {
    state: () => {
        return {user: null}
    },

    getters: {
        getUserName(state) {
            if (state.user) {
                return `${state.user.first_name} ${state.user.last_name} (${state.user.email})`;
            }
        },
        getUserId(state) {
            return state.user ? state.user.id : null;
        }
    },

    actions: {
        logOut() {
            this.user = null
            localStorage.removeItem('userToken')
        },
        async fetchUser() {
            const response = await apiFetch('/api/v1/auth/current-user/', {method: 'GET'})
            if (response.status === 200) {
                this.user = await response.json()
            }
        }
    },
})