import axios from "axios"
import { ACCESS_TOKEN } from "./constants"


const apiUrl = "/choreo-apis/djangoreactnote/backend/rest-api-be2/v1" //this is for deployment on choreo. not part of the main code


const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl, //this also included b/c of const apiUrl above. the main one is below commented
})

// const api = axios.create({
//     baseURL: import.meta.env.VITE_API_URL
// })

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default api