This example demonstrates erronous mouse events on OS-X.

On OS-X the following occurs:
   * The dialog continues to move even with the mouse outside of the window.
   * The dialog moves down when the mouse is moved upward.
   * The dialog moves up when the mouse is moved downward.
   * The dialog becomes disconnected from the mouse when you move the mouse back within the window.

Conclusion:
OS-X is mouse events differ from other platforms.
   * The absolute mouse values are being passed even with the mouse off the screen.
   * The Y values are inverted.
