export const apiFetch = async function (url, {method = 'GET', headers = {}, body = null, ...otherParams} = {}) {

    const token = localStorage.getItem('userToken')

    const requestHeaders = {
        'Content-Type': 'application/json',
        'Authorization': token ? `Bearer ${token}` : '',
        ...headers
    }

    const resp = await fetch(url,
        {
            method,
            headers: requestHeaders,
            body,
            ...otherParams
        }
    )

    return resp
}