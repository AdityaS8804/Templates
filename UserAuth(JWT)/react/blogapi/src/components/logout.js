import React, { useEffect } from 'react'
import axiosInstance from '../axios'
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min'

function logout() {
    useEffect(() => {
        const history = useHistory()
        const response = axiosInstance.post('user/logout/blacklist/', {
            refresh_token: localStorage.getItem('refresh_token')
        })
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        axiosInstance.defaults.headers['Authorization'] = null
        history.push('/')
    })

    return (
        <div>logout</div>
    )
}

export default logout