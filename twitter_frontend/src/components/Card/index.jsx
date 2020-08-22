import React, { useState } from "react";
import { Persona, PersonaSize, ActionButton } from "@fluentui/react";
import "./index.css";
import faker from "faker";

const TweetCard = () => {
  const [imageUrl] = useState(faker.image.avatar());
  return (
    <div className='tweet-card'>
      <div className='persona-container'>
        <Persona size={PersonaSize.regular} imageUrl={imageUrl} />
      </div>
      <div className='tweet-content-container'>
        <div className='tweet-top-row-container'>
          <div className='name'>Name </div>
          <div className='secondary-info ml10'>Username</div>
          <div className='secondary-info ml10'>Time </div>
        </div>
        <div className='tweet-text mt5'>
          Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum
          sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies
          nec, pellentesque eu, pretium.
        </div>
        <div className='like-comment-container mt5'>
          <ActionButton iconProps={{ iconName: "Heart" }} text='20' />
          <ActionButton iconProps={{ iconName: "CommentAdd" }} text='20' />
        </div>
      </div>
    </div>
  );
};

export default TweetCard;
