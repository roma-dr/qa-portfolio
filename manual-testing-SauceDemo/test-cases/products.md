## Products Module

### TC-PROD-001: Products page is displayed after login
**Priority:** High  
**Status:** Pass  
**Expected:** Products page is opened, list of products is visible  
**Actual:** Products page opened correctly (`standard_user`)

---

### TC-PROD-002: Sort products A to Z
**Priority:** Medium  
**Status:** Fail  
**Expected:** Products are sorted alphabetically from A to Z  
**Actual:** Sorting does not work on `problem_user` / `error_user` / `visual_user`

---

### TC-PROD-003: Sort products Z to A
**Priority:** Medium  
**Status:** Fail  
**Expected:** Products are sorted alphabetically from Z to A  
**Actual:** Sorting does not work

---

### TC-PROD-004: Sort products by price (low to high)
**Priority:** Medium  
**Status:** Fail  
**Expected:** Products are sorted by price ascending  
**Actual:** Sorting does not work

---

### TC-PROD-005: Sort products by price (high to low)
**Priority:** Medium  
**Status:** Fail  
**Expected:** Products are sorted by price descending  
**Actual:** Sorting does not work

---

### TC-PROD-006: Add one product to cart
**Priority:** High  
**Status:** Pass  
**Expected:** Button changes to “Remove”, cart counter shows 1  
**Actual:** Works correctly on `standard_user`

---

### TC-PROD-007: Add multiple products to cart
**Priority:** High  
**Status:** Pass  
**Expected:** Cart counter shows the correct number of added products  
**Actual:** Works correctly on `standard_user`
