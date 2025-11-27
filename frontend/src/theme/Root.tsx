import React, { useState, useEffect, ReactNode } from "react";
import ChatWidget from "../components/ChatWidget";

interface RootProps {
  children: ReactNode;
}

interface FabPosition {
  top: number;
  left: number;
}

export default function Root({ children }: RootProps): JSX.Element {
  // 1. Selection FAB State
  const [showSelectionFab, setShowSelectionFab] = useState<boolean>(false);
  const [fabPosition, setFabPosition] = useState<FabPosition>({
    top: 0,
    left: 0,
  });
  const [selectedText, setSelectedText] = useState<string>("");

  // 2. Chat Window State
  const [isChatOpen, setIsChatOpen] = useState<boolean>(false);

  // Logic: Handle Text Selection
  useEffect(() => {
    const handleMouseUp = () => {
      if (typeof window === "undefined") return;

      const selection = window.getSelection();
      const text = selection ? selection.toString().trim() : "";

      if (text.length > 0) {
        // User selected text -> Show Contextual FAB
        const range = selection!.getRangeAt(0);
        const rect = range.getBoundingClientRect();

        setFabPosition({
          top: rect.top + window.scrollY - 50,
          left: rect.left + rect.width / 2 - 40,
        });
        setSelectedText(text);
        setShowSelectionFab(true);
      } else {
        // User clicked away -> Hide Contextual FAB
        setTimeout(() => setShowSelectionFab(false), 200);
      }
    };

    if (typeof window !== "undefined") {
      document.addEventListener("mouseup", handleMouseUp);
    }
    return () => {
      if (typeof window !== "undefined")
        document.removeEventListener("mouseup", handleMouseUp);
    };
  }, []);

  const handleSelectionFabClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.stopPropagation();
    setShowSelectionFab(false);
    setIsChatOpen(true); // Open chat with context
  };

  return (
    <>
      {children}

      {/* --- 1. CONTEXTUAL BUTTON (Only shows on selection) --- */}
      {showSelectionFab && (
        <button
          style={{
            position: "absolute",
            top: `${fabPosition.top}px`,
            left: `${fabPosition.left}px`,
            zIndex: 9999,
            padding: "8px 16px",
            backgroundColor: "#25c2a0",
            color: "white",
            border: "none",
            borderRadius: "20px",
            cursor: "pointer",
            boxShadow: "0 4px 10px rgba(0,0,0,0.3)",
            fontWeight: "bold",
            animation: "fadeIn 0.2s",
          }}
          onMouseDown={(e) => e.preventDefault()} // Prevent clicking button from clearing selection
          onClick={handleSelectionFabClick}
        >
          Ask AI 🤖
        </button>
      )}

      {/* --- 2. PERMANENT TOGGLE BUTTON (Always visible) --- */}
      {!isChatOpen && (
        <button
          onClick={() => {
            setSelectedText(""); // Clear context for general chat
            setIsChatOpen(true);
          }}
          style={{
            position: "fixed",
            bottom: "20px",
            right: "20px",
            width: "60px",
            height: "60px",
            borderRadius: "50%",
            backgroundColor: "#25c2a0",
            color: "white",
            border: "none",
            boxShadow: "0 4px 12px rgba(0,0,0,0.3)",
            zIndex: 9998,
            cursor: "pointer",
            fontSize: "24px",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            transition: "transform 0.2s",
          }}
          onMouseEnter={(e) => (e.currentTarget.style.transform = "scale(1.1)")}
          onMouseLeave={(e) => (e.currentTarget.style.transform = "scale(1)")}
        >
          💬
        </button>
      )}

      {/* --- 3. THE CHAT WINDOW --- */}
      <ChatWidget
        isOpen={isChatOpen}
        onClose={() => setIsChatOpen(false)}
        initialContext={selectedText}
      />
    </>
  );
}
