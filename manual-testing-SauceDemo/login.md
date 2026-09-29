# Test Cases — Sauce Demo

## Login Module

### TC-LOGIN-001: Successful login with standard_user
**Priority:** High  
**Status:** Pass  
**Steps:**
1. Enter `standard_user` / `secret_sauce`
2. Click Login  
**Expected:** Redirect to Products page  
**Actual:** Redirected to Products page

---

### TC-LOGIN-002: Login with locked_out_user
**Priority:** High  
**Status:** Pass  
**Steps:**
1. Enter `locked_out_user` / `secret_sauce`
2. Click Login  
**Expected:** Error “Sorry, this user has been locked out.”  
**Actual:** Correct error message is displayed

---

### TC-LOGIN-003: Login with incorrect password
**Priority:** High  
**Status:** Pass  
**Steps:**
1. Enter `standard_user` / `wrong_password`
2. Click Login  
**Expected:** Error “Username and password do not match…”  
**Actual:** Correct error message is displayed

---

### TC-LOGIN-004: Login with empty fields
**Priority:** High  
**Status:** Pass  
**Steps:**
1. Leave both fields empty
2. Click Login  
**Expected:** Error “Username is required”  
**Actual:** Correct error message is displayed

---

### TC-LOGIN-005: Login with username only
**Priority:** Medium  
**Status:** Pass  
**Steps:**
1. Enter username only
2. Click Login  
**Expected:** Error “Password is required”  
**Actual:** Correct error message is displayed

---

### TC-LOGIN-006: Login with password only
**Priority:** Medium  
**Status:** Pass  
**Steps:**
1. Enter password only
2. Click Login  
**Expected:** Error “Username is required”  
**Actual:** Correct error message is displayed

---

### TC-LOGIN-007: Login with problem_user
**Priority:** Medium  
**Status:** Pass  
**Steps:**
1. Enter `problem_user` / `secret_sauce`
2. Click Login  
**Expected:** Login succeeds (UI issues may appear)  
**Actual:** Login succeeded

---

### TC-LOGIN-008: Login with performance_glitch_user
**Priority:** Low  
**Status:** Pass  
**Steps:**
1. Enter `performance_glitch_user` / `secret_sauce`
2. Click Login  
**Expected:** Login succeeds but with significant delay  
**Actual:** Login succeeded with long delay

---

### TC-LOGIN-009: Login with error_user
**Priority:** Medium  
**Status:** Pass  
**Steps:**
1. Enter `error_user` / `secret_sauce`
2. Click Login  
**Expected:** Login succeeds  
**Actual:** Login succeeded

---

### TC-LOGIN-010: Login with visual_user
**Priority:** Medium  
**Status:** Pass  
**Steps:**
1. Enter `visual_user` / `secret_sauce`
2. Click Login  
**Expected:** Login succeeds (visual issues may appear)  
**Actual:** Login succeeded