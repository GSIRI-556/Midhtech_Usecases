
/** @vitest-environment jsdom */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import "@testing-library/jest-dom/vitest";
import App from "../App";

describe("Claims Management App", () => {
  beforeEach(() => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => [],
      })
    );
  });

  afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
  });

  it("displays the Claims Management heading", () => {
    render(<App />);

    expect(
      screen.getByRole("heading", { name: "Claims Management" })
    ).toBeInTheDocument();
  });

  it("displays a message when no claims are available", () => {
    render(<App />);

    expect(screen.getByText("No claims available.")).toBeInTheDocument();
  });
});
