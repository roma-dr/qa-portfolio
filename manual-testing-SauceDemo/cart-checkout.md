## Cart & Checkout Module

### TC-CHECK-001: Successful full checkout
**Priority:** High  
**Status:** Pass  
**Expected:** Order confirmation page is shown  
**Actual:** Order completed successfully with products in cart

---

### TC-CHECK-002: Empty First Name
**Priority:** High  
**Status:** Pass  
**Expected:** Validation error appears  
**Actual:** Validation works on `standard_user`

---

### TC-CHECK-003: Empty Last Name
**Priority:** High  
**Status:** Pass  
**Expected:** Validation error appears  
**Actual:** Validation works on `standard_user`

---

### TC-CHECK-004: Empty Postal Code
**Priority:** High  
**Status:** Pass  
**Expected:** Validation error appears  
**Actual:** Validation works on `standard_user`

---

### TC-CHECK-005: All fields empty
**Priority:** High  
**Status:** Pass  
**Expected:** Validation error appears  
**Actual:** Validation works on `standard_user`

---

### TC-CHECK-006: Cancel on Information page
**Priority:** Medium  
**Status:** Pass  
**Expected:** Returns to Cart  
**Actual:** Works as expected

---

### TC-CHECK-007: Cancel on Overview page
**Priority:** Medium  
**Status:** Pass  
**Expected:** Returns to Products page (or Cart)  
**Actual:** Works as expected

---

### TC-CHECK-008: Verify prices and total on Overview
**Priority:** High  
**Status:** Pass  
**Expected:** Item prices, tax and total are calculated correctly  
**Actual:** Correct on `standard_user`

---

### TC-CHECK-009: Finish order and return to Products
**Priority:** Medium  
**Status:** Pass  
**Expected:** User returns to Products page, cart is empty  
**Actual:** Works as expected

---

### TC-CHECK-010: Postal Code accepts letters
**Priority:** Medium  
**Status:** Fail  
**Expected:** Should show validation error  
**Actual:** Letters are accepted (no proper validation)