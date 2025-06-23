# color-selector

## Metadata
- **Version**: 0.0.1
- **Description**: 
- **Category**: components

## Example Sections
1. **Default color selectors**
   - Description: 

## Examples
### Default color selector
- **Section**: Default color selectors
- **URL**: components/color-selector/color-input
- **Tags**: 
```tsx
import {
  offset,
  safePolygon,
  useDismiss,
  useFloating,
  useFocus,
  useHover,
  useInteractions,
  useRole,
} from '@floating-ui/react';
import { Input, Label, Button, Tooltip, Utility, UtilityFragment } from '@visa/nova-react';
import { VisaAccessibilityTiny } from '@visa/nova-icons-react';
import { useState } from 'react';


// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'color-input';

export const ColorInput = () => {
  const [isOpen, setIsOpen] = useState(false);

  const { x, y, strategy, refs, context } = useFloating({
    middleware: [offset(2)],
    open: isOpen,
    onOpenChange: setIsOpen,
    placement: 'right',
  });

  const dismiss = useDismiss(context);
  const focus = useFocus(context);
  const hover = useHover(context, { handleClose: safePolygon(), move: false });
  const role = useRole(context, { role: 'tooltip' });

  const { getReferenceProps, getFloatingProps } = useInteractions([dismiss, focus, hover, role]);

  return (
    <Utility vFlex vAlignItems="center" vGap={6}>
      <UtilityFragment vFlexGrow0 style={{ flexBasis: '5%' }}>
        <Input id={id} type="color" />
      </UtilityFragment>
      <Label htmlFor={id}>Label</Label>
      <Utility vAlignItems="center" vFlex vFlexCol vGap={2}>
      <Button 
        aria-labelledby={`${id}-label`}
        aria-label="Color selector accessibility information"
        colorScheme="tertiary"
        iconButton
        ref={refs.setReference} {...getReferenceProps()}>
          <VisaAccessibilityTiny rtl />
        </Button>
        {isOpen && (
        <Tooltip
          ref={refs.setFloating}
          style={{
            left: x,
            position: strategy,
            top: y,
            width: 'fit-content',
          }}
          {...getFloatingProps()}
        >
          For RGB, use values between 0-255. For HSL, use H values between 0-359, S and L values between 0-100%. For hex,
          use the format #RRGGBB and values between 0-9 or A-F.
        </Tooltip>
      )}
      </Utility>
    </Utility>
  );
};

```

## Property Sections
### input
- **Selector**: <Input />
- **Description**: 

