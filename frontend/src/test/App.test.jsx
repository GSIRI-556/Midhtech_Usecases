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

  it("displays the Login heading on initial load", () => {
    render(<App />);

    expect(
      screen.getByRole("heading", { name: "Login" })
    ).toBeInTheDocument();
  });

  it("displays the Register option on the Login page", () => {
    render(<App />);

    expect(
      screen.getByRole("button", { name: "Register" })
    ).toBeInTheDocument();
  });

  it("displays the empty claims message when Claims is selected", async () => {
    render(<App />);

    screen.getByRole("button", { name: "Claims" }).click();

    expect(
      await screen.findByText("No claims available.")
    ).toBeInTheDocument();
  });
});