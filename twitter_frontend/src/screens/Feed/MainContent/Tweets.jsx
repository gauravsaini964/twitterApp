import React, { useState, useLayoutEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Spinner, SpinnerSize } from "@fluentui/react";
import moment from "moment";

import { TweetCard } from "../../../components/";
import { fetchTweetList } from "../../../store/actions";

const TweetList = () => {
  const dispatch = useDispatch();
  const [isLoading, setIsLoading] = useState(true);
  const { tweets, noTweetsFound } = useSelector((state) => state.tweetReducer);

  useLayoutEffect(() => {
    dispatch(fetchTweetList());
    setIsLoading(false);
  }, []);

  const renderCard = () => {
    if (noTweetsFound) {
      return <div style={{ color: "gray" }}>Tweet Something to get the party started</div>;
    }
    const tweetList = tweets.map(
      ({ id, tweet, author_info, comments, likes, created_at, did_you_comment, did_you_like }) => {
        return (
          <div style={{ marginTop: 30 }}>
            <TweetCard
              key={id}
              name={`${author_info.first_name} ${author_info.last_name}`}
              commentsCount={comments.length}
              likesCount={likes}
              time={moment(created_at).fromNow(true)}
              tweetText={tweet}
              profilePic={author_info.profile_pic}
              didYouComment={did_you_comment}
              didYouLike={did_you_like}
              tweetId={id}
              username={`@${author_info.username}`}
            />
          </div>
        );
      },
    );
    return tweetList;
  };

  return <div style={{ width: "100%" }}>{isLoading ? <Spinner size={SpinnerSize.large} /> : renderCard()}</div>;
};

export default TweetList;
