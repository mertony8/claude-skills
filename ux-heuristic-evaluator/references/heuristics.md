# Nielsen's 10 Usability Heuristics — Reference

Use this reference when evaluating each heuristic. Each section contains the definition, what to look for, and common violations.

---

## 1. Visibility of System Status

**Definition:** The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time.

**What to look for:**
- Loading indicators when content is being fetched
- Progress bars for multi-step processes (checkout, signup, upload)
- Active/selected states in navigation showing current location
- Breadcrumbs showing the user's path
- Confirmation messages after actions (form submission, add to cart, delete)
- Real-time feedback on interactions (hover states, button press states)
- Page titles and URLs that reflect the current content
- Status indicators (online/offline, sync status, save status)

**Common violations:**
- No feedback after clicking a button (user doesn't know if it worked)
- Missing loading states — content appears to freeze
- No indication of current page in navigation
- Form submission with no confirmation message
- Progress-less multi-step flows (user doesn't know how many steps remain)
- Stale or cached data displayed without timestamp

---

## 2. Match Between System and the Real World

**Definition:** The design should speak the users' language. Use words, phrases, and concepts familiar to the user, rather than internal jargon. Follow real-world conventions, making information appear in a natural and logical order.

**What to look for:**
- User-facing language vs. technical/internal jargon
- Familiar icons and metaphors (trash can for delete, magnifying glass for search)
- Information ordered in a logical, expected way (chronological, alphabetical, by importance)
- Dates, currencies, and measurements in locally appropriate formats
- Labels and categories that match how users think about the content
- Natural mapping between controls and their effects

**Common violations:**
- Technical error codes shown to users (e.g., "Error 500: Internal Server Error")
- Developer terminology in UI (e.g., "null", "undefined", "query parameter")
- Unfamiliar abbreviations or acronyms without explanation
- Non-standard icons that don't match their conventional meaning
- Information organized by internal structure rather than user mental models

---

## 3. User Control and Freedom

**Definition:** Users often perform actions by mistake. They need a clearly marked "emergency exit" to leave the unwanted action without having to go through an extended process.

**What to look for:**
- Undo/redo functionality
- Cancel buttons on forms and dialogs
- Clear way to go back (browser back works, back links provided)
- Close buttons on modals, overlays, and popups
- Ability to dismiss notifications and alerts
- Exit paths from multi-step processes without losing all progress
- No forced actions (user can skip optional steps)

**Common violations:**
- No cancel button on forms or dialogs
- Modal popups with no close button or way to dismiss
- Multi-step processes that can't be abandoned without losing progress
- Destructive actions without undo (delete without confirmation)
- Forced registration or actions to access content
- Dead-end pages with no clear way to navigate elsewhere
- Back button doesn't work as expected (e.g., SPA navigation issues)

---

## 4. Consistency and Standards

**Definition:** Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform and industry conventions.

**What to look for:**
- Consistent visual design across pages (colors, fonts, spacing, button styles)
- Same terms used for same concepts throughout the site
- Standard UI patterns (navigation position, search bar location, footer content)
- Consistent interaction patterns (same action triggers same type of response everywhere)
- Internal consistency (within the site) and external consistency (with web conventions)
- Consistent header, footer, and navigation across all pages

**Common violations:**
- Different button styles for the same type of action on different pages
- Same functionality labeled differently (e.g., "Sign In" vs "Login" vs "Log On")
- Navigation structure that changes between pages
- Inconsistent use of colors or icons
- Breaking well-established web conventions (e.g., non-clickable logo, link text that isn't visually distinct)
- Different page layouts for structurally similar content

---

## 5. Error Prevention

**Definition:** Good error messages are important, but the best designs carefully prevent problems from occurring in the first place. Either eliminate error-prone conditions, or check for them and present users with a confirmation option before they commit to the action.

**What to look for:**
- Input constraints that prevent invalid data (date pickers, dropdowns, input masks)
- Confirmation dialogs before destructive or irreversible actions
- Inline validation that checks input before form submission
- Good defaults that reduce the chance of mistakes
- Clear required-field indicators
- Helpful placeholder text and input format hints
- Disabled states for unavailable actions (instead of allowing and then erroring)
- Search suggestions and autocomplete to prevent typos

**Common violations:**
- Free text fields where constrained inputs would prevent errors (e.g., text field for dates)
- No confirmation before delete or other destructive actions
- No real-time validation — all errors shown after submission
- Required fields not marked
- No format hints for complex inputs (phone numbers, dates, etc.)
- Allowing users to submit empty or clearly invalid forms

---

## 6. Recognition Rather Than Recall

**Definition:** Minimize the user's memory load by making elements, actions, and options visible. The user should not have to remember information from one part of the interface to another.

**What to look for:**
- Visible navigation (not hidden behind menus unnecessarily on desktop)
- Persistent labels on form fields (not just placeholder text that disappears)
- Recently viewed or search history features
- Contextual information displayed where needed (not requiring memory from other pages)
- Visible action buttons rather than hidden gestures or shortcuts
- Autocomplete and suggestions
- Visual cues and icons alongside text labels

**Common violations:**
- Form fields with only placeholder text (no persistent label — label disappears when typing)
- Desktop navigation hidden behind hamburger menus when space is available
- Users required to remember codes, IDs, or information from previous steps
- Important actions only accessible through right-click or keyboard shortcuts with no visual cue
- Comparison features that require remembering details from other pages

---

## 7. Flexibility and Efficiency of Use

**Definition:** Shortcuts — hidden from novice users — may speed up the interaction for the expert user so that the design can cater to both inexperienced and experienced users.

**What to look for:**
- Keyboard shortcuts for power users
- Search functionality with good results
- Filters and sorting options
- Breadcrumbs for quick navigation
- Skip links for accessibility
- Customization or personalization options
- Touch gestures on mobile
- Bulk actions for repetitive tasks
- Quick actions or shortcuts for frequent tasks

**Common violations:**
- No search functionality on content-heavy sites
- No keyboard navigation support
- Inability to filter or sort content
- No shortcuts for frequent users (every interaction requires full workflow)
- No skip navigation links for screen readers
- One-size-fits-all approach with no accommodation for different expertise levels

---

## 8. Aesthetic and Minimalist Design

**Definition:** Interfaces should not contain information that is irrelevant or rarely needed. Every extra unit of information in an interface competes with the relevant units of information and diminishes their relative visibility.

**What to look for:**
- Clear visual hierarchy — what's most important stands out
- Focused content — each page/section has a clear purpose
- Appropriate use of whitespace
- No excessive decorative elements that compete with content
- Concise text — no unnecessary verbosity
- Clean, uncluttered layouts
- Progressive disclosure (showing details on demand rather than all at once)

**Common violations:**
- Cluttered layouts with too many competing elements
- Excessive text that could be more concise
- Decorative elements that distract from core content
- Multiple competing calls-to-action on the same page
- Irrelevant content or advertisements that overshadow primary content
- Information overload — everything shown at once with no hierarchy
- Auto-playing media or animations that distract from the user's task

---

## 9. Help Users Recognize, Diagnose, and Recover from Errors

**Definition:** Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution.

**What to look for:**
- Error messages in plain, human-readable language
- Specific indication of what went wrong (which field, what the problem is)
- Constructive suggestions for fixing the error
- Visual treatment that makes errors noticeable (color, icons, position)
- Error messages placed near the source of the error (not just at the top of the page)
- 404 pages that help users find what they were looking for

**Common violations:**
- Generic error messages ("Something went wrong", "An error occurred")
- Technical error codes shown to users (HTTP 500, Error Code: E_FAIL)
- No indication of which field caused a form validation error
- Error messages that only say what's wrong but don't suggest a fix
- Errors not visually prominent enough to notice
- 404 pages with no helpful navigation or search
- Errors that disappear too quickly to read

---

## 10. Help and Documentation

**Definition:** It's best if the system doesn't need any additional explanation. However, it may be necessary to provide documentation to help users understand how to complete their tasks.

**What to look for:**
- Help section, FAQ, or knowledge base
- Searchable documentation
- Contextual help (tooltips, inline hints, info icons)
- Onboarding flows for new users
- Contact support options (chat, email, phone)
- Step-by-step guides for complex tasks
- Help content that's task-focused and concise

**Common violations:**
- No help section or documentation at all
- Help content that's not searchable
- Documentation organized by features rather than user tasks
- Help buried deep in the navigation or hard to find
- No contextual help where users are likely to need it
- Outdated or inaccurate documentation
- No way to contact a human for support
