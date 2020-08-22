import qs from "querystring";

const responseChecker = async (response) => {
  let error = "";
  let data = {};
  let statusCode = null;
  if (!response.ok) {
    error = "Something went wrong";
    statusCode = response.status;
  } else {
    statusCode = response.status;
    data = await response.json();
  }
  return { statusCode, error, data };
};

const useFetch = (baseURL, authHeader = null, key = "dsHSYWhbdas17876735Hdada") => {
  const defaultHeader = {
    Accept: "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
    // "Content-Type": "application/json",
    key,
    Authorization: authHeader,
  };

  const customFetch = (url, method = "GET", body = false, headers = defaultHeader) => {
    const options = {
      method,
      headers,
      // credentials: "include",
    };
    if (body) options.body = qs.stringify(body);
    return fetch(url, options);
  };
  const get = async (endpoint) => {
    const token = localStorage.getItem("token");
    defaultHeader.Authorization = token;
    const url = `${baseURL}${endpoint}`;
    const response = await customFetch(url, "GET");
    return responseChecker(response);
  };
  const post = async (endpoint, body = {}) => {
    const token = localStorage.getItem("token");
    defaultHeader.Authorization = token;
    const url = `${baseURL}${endpoint}`;
    const response = await customFetch(url, "POST", body);
    return responseChecker(response);
  };
  const put = async (endpoint, body = {}) => {
    const token = localStorage.getItem("token");
    defaultHeader.Authorization = token;
    const url = `${baseURL}${endpoint}`;
    const response = await customFetch(url, "PUT", body);
    return responseChecker(response);
  };
  return {
    get,
    post,
    put,
  };
};
export default useFetch;
