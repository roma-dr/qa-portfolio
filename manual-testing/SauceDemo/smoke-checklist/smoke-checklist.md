# Smoke Checklist — Sauce Demo

**Application:** [https://www.saucedemo.com](https://www.saucedemo.com)  
**Type:** E-commerce demo application  
**Browser:** Chrome, Safari  

---

## 1. Purpose

This smoke checklist verifies the critical user flow of the application.  
The goal is to quickly confirm that the main functionality is available and working before deeper testing.

---

## 2. Scope

**In scope:**
- Login
- Viewing products
- Adding product to cart
- Checkout process
- Logout

**Out of scope:**
- Special demo users (`problem_user`, `error_user`, `visual_user`, etc.)
- Negative scenarios
- UI/UX detailed checks
- Cross-browser testing
- Performance testing

---

## 3. Smoke Test Steps

| # | Step | Expected Result | Status | Notes |
|---|------|-----------------|--------|-------|
| 1 | Open https://www.saucedemo.com | Login page is displayed | Pass | |
| 2 | Login with `standard_user` / `secret_sauce` | User is redirected to Products page | Pass | |
| 3 | Verify Products page is loaded | List of products is visible | Pass | |
| 4 | Add one product to cart | Button changes to "Remove", cart counter shows 1 | Pass | |
| 5 | Open the cart | Added product is displayed in the cart | Pass | |
| 6 | Click Checkout | Checkout information page is opened | Pass | |
| 7 | Fill First Name, Last Name, Postal Code and continue | Overview page is displayed | Pass | |
| 8 | Click Finish | Order confirmation page is shown | Pass | |
| 9 | Click Back Home / Logout | User is logged out and returned to Login page | Pass | |

---

## 4. Result

**Smoke status:** Passed with issues

**Summary:**  
The main happy path (Login → Add to cart → Checkout → Logout) works correctly with `standard_user`. Multiple issues were also found when using special demo accounts (`problem_user`, `error_user`, `visual_user`, `performance_glitch_user`). These are documented in the bug reports section and were not part of this smoke run.

**Known issue found during smoke:**
- User can complete checkout with an empty cart (see BUG-001). This is a high-severity functional issue in the core flow.

---

## 5. Conclusion

Smoke test is considered **passed with issues**.  
The application is available for further testing, but BUG-001 (empty cart checkout) should be addressed as it affects the core business flow.
