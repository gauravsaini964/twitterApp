import React, { useState } from "react";
import {
  Persona,
  PersonaSize,
  ActionButton,
  Dialog,
  PrimaryButton,
  DefaultButton,
  DialogFooter,
  DialogType,
  TextField,
} from "@fluentui/react";
import { tweetAPI } from "../../utilities/api";

import "./index.css";

const TweetCard = ({
  profilePic,
  username,
  tweetText,
  time,
  name,
  likesCount,
  commentsCount,
  didYouLike,
  didYouComment,
  tweetId,
}) => {
  const [likes, setLikes] = useState(likesCount);
  const [comments, setComments] = useState(commentsCount);
  const [commentText, setCommentText] = useState("");
  const [didYouLikedThisTweet, setDidYouLikedThisTweet] = useState(didYouLike);
  const [didYouCommentThisTweet, setDidYouCommentThisTweet] = useState(didYouComment);
  const [isCommentBoxHidden, setIsCommentBoxHidden] = useState(true);
  const [finalSubmitDisabled, setFinalSubmitDisabled] = useState(true);

  const onCommentButtonPress = () => {
    setIsCommentBoxHidden(false);
  };

  const onCommentChange = (e, value) => {
    setCommentText(value);
    setFinalSubmitDisabled(false);
    if (!value) {
      setFinalSubmitDisabled(true);
    }
  };

  const modelProps = {
    isBlocking: false,
    styles: { main: { maxWidth: 450 } },
  };
  const dialogContentProps = {
    type: DialogType.largeHeader,
    title: "Add your thoughts...",
  };

  const onLikeButtonPress = async () => {
    console.log(didYouLikedThisTweet);
    if (!didYouLikedThisTweet) {
      console.log("here first?");
      const { statusCode } = await tweetAPI.post("/v1/likes/", { tweet_id: tweetId });
      if (statusCode === 201) {
        setDidYouLikedThisTweet(true);
        setLikes(likes + 1);
      }
    } else {
      console.log("here 2nd?");
      const { statusCode } = await tweetAPI.deleteMethod("/v1/likes/", { tweet_id: tweetId });
      if (statusCode === 200) {
        setDidYouLikedThisTweet(false);
        setLikes(likes - 1);
      }
    }
  };

  const onCommentSubmit = async () => {
    const { statusCode } = await tweetAPI.post("/v1/comment/", { tweet_id: tweetId, comment: commentText });
    if (statusCode === 201) {
      setDidYouCommentThisTweet(true);
      setIsCommentBoxHidden(true);
      setComments(comments + 1);
    }
  };

  return (
    <div className='tweet-card'>
      <div className='persona-container ml20'>
        <Persona size={PersonaSize.large} imageUrl={profilePic} />
      </div>
      <div className='tweet-content-container'>
        <div className='tweet-top-row-container'>
          <div className='name'>{name}</div>
          <div className='secondary-info ml10'>{username}</div>
          <div className='secondary-info ml10'>{time}</div>
        </div>
        <div className='tweet-text mt5'>{tweetText}</div>
        <div className='like-comment-container mt5'>
          <ActionButton
            iconProps={{ iconName: didYouLikedThisTweet ? "HeartFill" : "Heart" }}
            text={likes}
            onClick={onLikeButtonPress}
          />
          <ActionButton
            iconProps={{ iconName: didYouCommentThisTweet ? "CommentSolid" : "CommentAdd" }}
            text={comments}
            onClick={onCommentButtonPress}
          />
        </div>
        <div>
          <Dialog hidden={isCommentBoxHidden} modalProps={modelProps} dialogContentProps={dialogContentProps}>
            <TextField multiline onChange={onCommentChange} />
            <DialogFooter>
              <PrimaryButton text='Comment' onClick={onCommentSubmit} disabled={finalSubmitDisabled} />
              <DefaultButton text='Cancel' onClick={() => setIsCommentBoxHidden(true)} />
            </DialogFooter>
          </Dialog>
        </div>
      </div>
    </div>
  );
};

export default TweetCard;
