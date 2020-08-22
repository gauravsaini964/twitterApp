import * as ACTION_TYPE from "../actions/types";

const initialState = {
  tweets: [],
  noTweetsFound: false,
};

const tweetReducer = (state = initialState, action) => {
  switch (action.type) {
    case ACTION_TYPE.SET_TWEET_LIST:
      return {
        ...state,
        tweets: action.payload,
        noTweetsFound: false,
      };
    case ACTION_TYPE.NO_TWEETS_FOUND:
      return {
        ...state,
        noTweetsFound: true,
      };

    default:
      return state;
  }
};

export default tweetReducer;
