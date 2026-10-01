# Bug Reports — Sauce Demo

## BUG-001: User can complete checkout with an empty cart
**Severity:** High  
**Priority:** High  
**User:** standard_user  

**Steps:**
1. Login with `standard_user`
2. Open cart without adding products
3. Click Checkout → fill form → Finish

**Actual:** Order is completed successfully.  
**Expected:** Checkout should be blocked when cart is empty.

---

## BUG-002: All products show the same dog image
**Severity:** High  
**Priority:** High  
**User:** problem_user  

**Actual:** Every product displays the same dog image.  
**Expected:** Each product has a unique correct image.

---

## BUG-003: Product name and description mismatch
**Severity:** High  
**Priority:** High  
**User:** problem_user  

**Actual:** Clicking a product opens a completely different item.  
**Expected:** Correct product details should open.

---

## BUG-004: Add to cart button broken on product details page
**Severity:** High  
**Priority:** High  
**User:** problem_user  

**Actual:** Button does not add product to cart.  
**Expected:** Product should be added successfully.

---

## BUG-005: Sorting does not work
**Severity:** High  
**Priority:** High  
**User:** problem_user, error_user  

**Actual:**  
- Sorting has no effect (`problem_user`)  
- Error message appears (`error_user`): “Sorting is broken!…”  

**Expected:** Sorting should work correctly.

---

## BUG-006: Last Name field overwrites First Name
**Severity:** High  
**Priority:** High  
**User:** problem_user  

**Actual:** Typing in Last Name modifies/overwrites First Name.  
**Expected:** Fields should work independently.

---

## BUG-007: Last Name field does not accept input
**Severity:** High  
**Priority:** High  
**User:** error_user  

**Actual:** Keyboard input is ignored in Last Name field.  
**Expected:** User can type Last Name normally.

---

## BUG-008: Significant performance delay
**Severity:** Medium  
**Priority:** Medium  
**User:** performance_glitch_user  

**Actual:** Very long delays after every action.  
**Expected:** Normal response time.

---

## BUG-009: Cart icon overlaps content
**Severity:** Medium  
**Priority:** Medium  
**User:** visual_user  

**Actual:** Cart icon is misplaced and covers page content.  
**Expected:** Correct position without overlapping.

---

## BUG-010: Prices change on every load and sort
**Severity:** Medium  
**Priority:** Medium  
**User:** visual_user  

**Actual:** Product prices change randomly after refresh or sorting.  
**Expected:** Prices remain stable.

---

## BUG-011: Checkout button is misplaced
**Severity:** Medium  
**Priority:** Medium  
**User:** visual_user  

**Actual:** Checkout button is shifted and incorrectly positioned.  
**Expected:** Button should be aligned correctly.

---

## BUG-012: First product always shows dog image
**Severity:** Medium  
**Priority:** Medium  
**User:** visual_user  

**Actual:** The first product on the list always has a dog image.  
**Expected:** Correct product image should be shown.

---

## BUG-013: About page returns 404
**Severity:** Low  
**Priority:** Low  
**User:** problem_user  

**Steps:**
1. Open menu
2. Click About

**Actual:** 404 error page is shown.  
**Expected:** About page should open successfully.

---

## BUG-014: Product cards not clickable in Dynamic Catalog
**Severity:** Medium  
**Priority:** Medium  

**Actual:** Product cards in Dynamic Catalog section are not clickable.  
**Expected:** Cards should open product details.

---

## BUG-015: Infinite scroll with duplicate products (Lazy Load)
**Severity:** Medium  
**Priority:** Medium  

**Actual:** Scrolling down endlessly loads the same products again and again.  
**Expected:** Should load new unique products or stop at the end of the list.
