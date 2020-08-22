import * as ACTION_TYPE from "../actions/types";

const initialState = {
  tweets: [],
};

const tweetReducer = (state = initialState, action) => {
  switch (action.type) {
    case ACTION_TYPE.SET_TWEET_LIST:
      return {
        ...state,
        tweets: action.payload,
      };

    default:
      return state;
  }
};

export default tweetReducer;
