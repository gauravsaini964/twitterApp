import * as ACTION_TYPE from "./types";
import { tweetAPI } from "../../utilities/api";

export const setUserInfo = (payload) => (dispatch) => {
  dispatch({ type: ACTION_TYPE.SET_USER_INFO, payload });
};

export const fetchTweetList = () => async (dispatch) => {
  const { data, statusCode } = await tweetAPI.get("/tweet");
  if (statusCode === 404) {
    dispatch({ type: ACTION_TYPE.NO_TWEETS_FOUND });
  } else if (statusCode !== 200) {
    alert("Failed to fetch list of tweet");
  } else {
    dispatch({ type: ACTION_TYPE.SET_TWEET_LIST, payload: data.result });
  }
};

export const postTweet = (formData) => async (dispatch) => {
  const { statusCode } = await tweetAPI.post("/tweet/", formData);
  if (statusCode !== 201) {
    alert("Failed to create tweet");
  } else {
    dispatch({ type: ACTION_TYPE.POST_TWEET });
    dispatch(fetchTweetList());
  }
};
