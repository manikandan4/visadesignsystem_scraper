# tooltip

## Metadata
- **Version**: 0.0.1
- **Description**: Short message communicating the function or context of a control or object.
- **Category**: components

## Example Sections
1. **Default tooltips**
   - Description: 

## Examples
### Top-positioned tooltip
- **Section**: Default tooltips
- **URL**: components/tooltip/top-tooltip
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
import { Button, Tooltip, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const TopTooltip = () => {
  const [isOpen, setIsOpen] = useState(false);

  const { x, y, strategy, refs, context } = useFloating({
    middleware: [offset(2)],
    open: isOpen,
    onOpenChange: setIsOpen,
    placement: 'top',
  });

  const dismiss = useDismiss(context);
  const focus = useFocus(context);
  const hover = useHover(context, { handleClose: safePolygon(), move: false });
  const role = useRole(context, { role: 'tooltip' });

  const { getReferenceProps, getFloatingProps } = useInteractions([dismiss, focus, hover, role]);

  return (
    <Utility vFlex vJustifyContent="center" vMargin={24}>
      <Button ref={refs.setReference} {...getReferenceProps()}>
        Primary action
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
          This is a tooltip
        </Tooltip>
      )}
    </Utility>
  );
};

```

### Bottom-positioned tooltip
- **Section**: Default tooltips
- **URL**: components/tooltip/bottom-tooltip
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
import { Button, Tooltip, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const BottomTooltip = () => {
  const [isOpen, setIsOpen] = useState(false);

  const { x, y, strategy, refs, context } = useFloating({
    middleware: [offset(2)],
    open: isOpen,
    onOpenChange: setIsOpen,
    placement: 'bottom',
  });

  const dismiss = useDismiss(context);
  const focus = useFocus(context);
  const hover = useHover(context, { handleClose: safePolygon(), move: false });
  const role = useRole(context, { role: 'tooltip' });

  const { getReferenceProps, getFloatingProps } = useInteractions([dismiss, focus, hover, role]);

  return (
    <Utility vFlex vJustifyContent="center" vMargin={24}>
      <Button ref={refs.setReference} {...getReferenceProps()}>
        Primary action
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
          This is a tooltip
        </Tooltip>
      )}
    </Utility>
  );
};

```

### Left-positioned tooltip
- **Section**: Default tooltips
- **URL**: components/tooltip/left-tooltip
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
import { Button, Tooltip, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const LeftTooltip = () => {
  const [isOpen, setIsOpen] = useState(false);

  const { x, y, strategy, refs, context } = useFloating({
    middleware: [offset(2)],
    open: isOpen,
    onOpenChange: setIsOpen,
    placement: 'left',
  });

  const dismiss = useDismiss(context);
  const focus = useFocus(context);
  const hover = useHover(context, { handleClose: safePolygon(), move: false });
  const role = useRole(context, { role: 'tooltip' });

  const { getReferenceProps, getFloatingProps } = useInteractions([dismiss, focus, hover, role]);

  return (
    <Utility vFlex vJustifyContent="center" vMargin={24}>
      <Button ref={refs.setReference} {...getReferenceProps()}>
        Primary action
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
          This is a tooltip
        </Tooltip>
      )}
    </Utility>
  );
};

```

### Right-positioned tooltip
- **Section**: Default tooltips
- **URL**: components/tooltip/right-tooltip
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
import { Button, Tooltip, Utility } from '@visa/nova-react';
import { useState } from 'react';

export const RightTooltip = () => {
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
    <Utility vFlex vJustifyContent="center" vMargin={24}>
      <Button ref={refs.setReference} {...getReferenceProps()}>
        Primary action
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
          This is a tooltip
        </Tooltip>
      )}
    </Utility>
  );
};

```

## Property Sections
### Tooltip
- **Selector**: <Tooltip />
- **Description**: Short message communicating the function or context of a control or object.

## Properties
### ref
- **Section**: Tooltip
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Tooltip
- **Type**: ElementType
- **Default**: span
- **Required**: false
- **Description**: Tag of Component

