## Negative & Special Users

### TC-NEG-001: Logout
**Priority:** High  
**Status:** Pass  
**Expected:** Redirect to Login page  
**Actual:** Redirect works

---

### TC-NEG-002: Direct access to /inventory.html without login
**Priority:** High  
**Status:** Pass  
**Expected:** Redirect to Login page  
**Actual:** Redirect works

---

### TC-NEG-003: Direct access to /cart.html without login
**Priority:** High  
**Status:** Pass  
**Expected:** Redirect to Login page  
**Actual:** Redirect works

---

### TC-NEG-004: Behavior of problem_user
**Priority:** High  
**Status:** Fail  
**Expected:** Multiple UI and functional issues  
**Actual:** Many bugs found (images, sorting, add to cart, form fields)

---

### TC-NEG-005: Behavior of error_user
**Priority:** High  
**Status:** Fail  
**Expected:** Sorting error, problems with form input  
**Actual:** Sorting broken + Last Name field does not accept input

---

### TC-NEG-006: Behavior of visual_user
**Priority:** Medium  
**Status:** Fail  
**Expected:** Layout issues, overlapping elements, changing prices  
**Actual:** Cart icon overlap, wrong button position, changing prices, dog image

---

### TC-NEG-007: Behavior of performance_glitch_user
**Priority:** Medium  
**Status:** Fail  
**Expected:** Noticeable delays in all actions  
**Actual:** Very long delays confirmed

---

### TC-NEG-008: Browser Back after logout
**Priority:** Medium  
**Status:** Pass  
**Expected:** Protected pages are not accessible  
**Actual:** Works as expected