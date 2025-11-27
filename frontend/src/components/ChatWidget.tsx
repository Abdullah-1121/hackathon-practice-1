import React, { useState, useEffect, useRef } from "react";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,
} from "@chatscope/chat-ui-kit-react";

interface ChatWidgetProps {
  isOpen: boolean;
  onClose: () => void;
  initialContext: string;
}

interface ChatMessage {
  message: string;
  sender: "user" | "assistant" | "system";
  direction: "outgoing" | "incoming";
  position?: "single" | "first" | "normal" | "last";
}

export default function ChatWidget({
  isOpen,
  onClose,
  initialContext,
}: ChatWidgetProps): JSX.Element | null {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      message:
        "Hello! Highlight text to ask me about it, or just ask a general question.",
      sender: "assistant",
      direction: "incoming",
      position: "single",
    },
  ]);
  const [isTyping, setIsTyping] = useState<boolean>(false);

  const hasSentContext = useRef<boolean>(false);

  useEffect(() => {
    if (isOpen && initialContext && !hasSentContext.current) {
      handleSend(`Explain this context: "${initialContext}"`);
      hasSentContext.current = true;
    }
    if (!isOpen) {
      hasSentContext.current = false;
    }
  }, [isOpen, initialContext]);

  const handleSend = async (text: string) => {
    const newUserMessage: ChatMessage = {
      message: text,
      sender: "user",
      direction: "outgoing",
      position: "single",
    };
    setMessages((prev) => [...prev, newUserMessage]);
    setIsTyping(true);

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query: text,
          context: initialContext || null,
        }),
      });

      if (!response.ok) throw new Error("API Error");

      const data = await response.json();

      const newAiMessage: ChatMessage = {
        message: data.content,
        sender: "assistant",
        direction: "incoming",
        position: "single",
      };
      setMessages((prev) => [...prev, newAiMessage]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        {
          message: "Error: Could not connect to the Brain. Is uvicorn running?",
          sender: "system",
          direction: "incoming",
          position: "single",
        },
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div
      style={{
        position: "fixed",
        bottom: "80px",
        right: "20px",
        width: "350px",
        height: "500px",
        zIndex: 10000,
        boxShadow: "0 0 20px rgba(0,0,0,0.2)",
        borderRadius: "12px",
        overflow: "hidden",
        backgroundColor: "white",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <div
        style={{
          backgroundColor: "#25c2a0",
          padding: "10px",
          color: "white",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <strong>Cybernetic Book AI</strong>
        <button
          onClick={onClose}
          style={{
            background: "none",
            border: "none",
            color: "white",
            cursor: "pointer",
            fontSize: "18px",
          }}
        >
          ✖
        </button>
      </div>
      <div style={{ flex: 1, overflow: "hidden" }}>
        <MainContainer>
          <ChatContainer>
            <MessageList
              typingIndicator={
                isTyping ? <TypingIndicator content="Thinking..." /> : null
              }
            >
              {messages.map((msg, i) => (
                // @ts-ignore
                <Message key={i} model={msg} />
              ))}
            </MessageList>
            <MessageInput placeholder="Ask a question..." onSend={handleSend} />
          </ChatContainer>
        </MainContainer>
      </div>
    </div>
  );
}
