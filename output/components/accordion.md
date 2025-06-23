# accordion

## Metadata
- **Version**: 0.0.1
- **Description**: Sets of vertical headers that reveal or hide the accordion panel.
- **Category**: components

## Example Sections
1. **Individual accordions**
   - Description: 
2. **Multi-select accordion groups**
   - Description: 
3. **Single-select accordion groups**
   - Description: 
4. **Custom accordion groups**
   - Description: 

## Examples
### Default accordion
- **Section**: Individual accordions
- **URL**: components/accordion/collapsed-accordion
- **Tags**: docs
```tsx
import { Accordion, AccordionHeading, AccordionPanel, AccordionToggleIcon, Typography } from '@visa/nova-react';

export const CollapsedAccordion = () => {
  return (
    <Accordion>
      <AccordionHeading buttonSize="large" colorScheme="secondary">
        <AccordionToggleIcon />
        Accordion title
      </AccordionHeading>
      <AccordionPanel>
        <Typography>This is required text that describes the accordion section in more detail.</Typography>
      </AccordionPanel>
    </Accordion>
  );
};

```

### Disabled accordion
- **Section**: Individual accordions
- **URL**: components/accordion/collapsed-disabled-accordion
- **Tags**: docs
```tsx
import { Accordion, AccordionHeading, AccordionPanel, AccordionToggleIcon, Typography } from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'collapsed-disabled-accordion';

export const CollapsedDisabledAccordion = () => {
  const expanded = false;

  return (
    <Accordion id={id} tag="div">
      <AccordionHeading
        aria-controls={`${id}-accordion-panel`}
        aria-expanded={expanded}
        disabled
        buttonSize="large"
        colorScheme="secondary"
        id={`${id}-accordion-header`}
        tag="button"
      >
        <AccordionToggleIcon accordionOpen={expanded} />
        Accordion title
      </AccordionHeading>
      <AccordionPanel aria-hidden={!expanded} id={`${id}-accordion-panel`}>
        <Typography>This is required text that describes the accordion section in more detail.</Typography>
      </AccordionPanel>
    </Accordion>
  );
};

```

### Accordion with icon
- **Section**: Individual accordions
- **URL**: components/accordion/with-icon-accordion
- **Tags**: docs
```tsx
import { VisaCloudLow } from '@visa/nova-icons-react';
import { Accordion, AccordionHeading, AccordionPanel, AccordionToggleIcon, Typography } from '@visa/nova-react';

export const WithIconAccordion = () => {
  return (
    <Accordion>
      <AccordionHeading buttonSize="large" colorScheme="secondary">
        <AccordionToggleIcon />
        <VisaCloudLow />
        Accordion title
      </AccordionHeading>
      <AccordionPanel>
        <Typography>This is required text that describes the accordion section in more detail.</Typography>
      </AccordionPanel>
    </Accordion>
  );
};

```

### Accordion with badge
- **Section**: Individual accordions
- **URL**: components/accordion/with-badge-accordion
- **Tags**: docs
```tsx
import { VisaSuccessTiny } from '@visa/nova-icons-react';
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Badge,
  Typography,
  UtilityFragment,
} from '@visa/nova-react';

export const WithBadgeAccordion = () => {
  return (
    <Accordion>
      <UtilityFragment vAlignItems="center">
        <AccordionHeading buttonSize="large" colorScheme="secondary">
          {/* TODO: Remove this style tag after nova-styles fix */}
          <AccordionToggleIcon style={{ alignSelf: 'center' }} />
          Accordion title
          <UtilityFragment vMarginLeft="auto">
            <Badge badgeType="stable">
              <VisaSuccessTiny />
              Label
            </Badge>
          </UtilityFragment>
        </AccordionHeading>
      </UtilityFragment>
      <AccordionPanel>
        <Typography>This is required text that describes the accordion section in more detail.</Typography>
      </AccordionPanel>
    </Accordion>
  );
};

```

### Subtle accordion
- **Section**: Individual accordions
- **URL**: components/accordion/subtle-accordion
- **Tags**: docs
```tsx
import { CSSProperties } from 'react';
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  UtilityFragment,
} from '@visa/nova-react';

export const SubtleAccordion = () => {
  return (
    <Accordion>
      <UtilityFragment vGap={2}>
        <AccordionHeading
          className="v-typography-body-2-medium"
          colorScheme="tertiary"
          style={
            {
              '--v-accordion-foreground-initial': 'var(--palette-default-active)',
              '--v-button-default-background': 'transparent',
            } as CSSProperties
          }
        >
          <AccordionToggleIcon />
          Accordion title
        </AccordionHeading>
      </UtilityFragment>
      <UtilityFragment vPaddingHorizontal={32}>
        <AccordionPanel
          style={
            {
              '--v-accordion-panel-background-color': 'transparent',
              '--v-accordion-panel-border-size': '0px',
            } as CSSProperties
          }
        >
          <Typography>This is required text that describes the accordion section in more detail.</Typography>
        </AccordionPanel>
      </UtilityFragment>
    </Accordion>
  );
};

```

### Disabled subtle accordion
- **Section**: Individual accordions
- **URL**: components/accordion/disabled-subtle-accordion
- **Tags**: docs
```tsx
import { CSSProperties } from 'react';
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  UtilityFragment,
} from '@visa/nova-react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'disabled-subtle-accordion';

export const DisabledSubtleAccordion = () => {
  const expanded = false;

  return (
    <Accordion tag="div">
      <UtilityFragment vGap={2}>
        <AccordionHeading
          aria-controls={`${id}-accordion-panel`}
          aria-expanded={expanded}
          buttonSize="large"
          disabled
          colorScheme="tertiary"
          id={`${id}-accordion-header`}
          tag="button"
        >
          <AccordionToggleIcon accordionOpen={expanded} />
          <Typography variant="body-2-medium">Accordion title</Typography>
        </AccordionHeading>
      </UtilityFragment>
      <UtilityFragment vPaddingHorizontal={32}>
        <AccordionPanel
          aria-hidden={!expanded}
          id={`${id}-accordion-panel`}
          style={
            {
              '--v-accordion-panel-background-color': 'transparent',
              '--v-accordion-panel-border-size': '0px',
            } as CSSProperties
          }
        >
          <Typography>This is required text that describes the accordion section in more detail.</Typography>
        </AccordionPanel>
      </UtilityFragment>
    </Accordion>
  );
};

```

### Subtle accordion with icon
- **Section**: Individual accordions
- **URL**: components/accordion/subtle-accordion-with-icon
- **Tags**: 
```tsx
import { CSSProperties } from 'react';
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  UtilityFragment,
} from '@visa/nova-react';
import { VisaCloudLow } from '@visa/nova-icons-react';

export const SubtleAccordionWithIcon = () => {
  return (
    <Accordion>
      <UtilityFragment vGap={2}>
        <AccordionHeading
          className="v-typography-body-2-medium"
          colorScheme="tertiary"
          style={
            {
              '--v-accordion-foreground-initial': 'var(--palette-default-active)',
              '--v-button-default-background': 'transparent',
            } as CSSProperties
          }
        >
          <AccordionToggleIcon />
          <VisaCloudLow />
          Accordion title
        </AccordionHeading>
      </UtilityFragment>
      <UtilityFragment vPaddingHorizontal={32}>
        <AccordionPanel
          style={
            {
              '--v-accordion-panel-background-color': 'transparent',
              '--v-accordion-panel-border-size': '0px',
            } as CSSProperties
          }
        >
          <Typography>This is required text that describes the accordion section in more detail.</Typography>
        </AccordionPanel>
      </UtilityFragment>
    </Accordion>
  );
};

```

### Default multi-select accordion group
- **Section**: Multi-select accordion groups
- **URL**: components/accordion/default-multi-select-accordion-group
- **Tags**: docs
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
} from '@visa/nova-react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-multi-select-accordion-group-example';

export const DefaultMultiSelectAccordionGroup = () => {
  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => (
        <Accordion key={`${id}-${index}`}>
          <AccordionHeading buttonSize="large" colorScheme="secondary">
            <AccordionToggleIcon />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel>
            <Typography>{accordion.content}</Typography>
          </AccordionPanel>
        </Accordion>
      ))}
    </Utility>
  );
};

```

### Multi-select accordion group with accordion expanded by default
- **Section**: Multi-select accordion groups
- **URL**: components/accordion/multi-select-accordion-group-with-expanded
- **Tags**: 
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
} from '@visa/nova-react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'multi-select-accordion-group-with-expanded';

export const MultiSelectAccordionGroupWithExpanded = () => {
  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => (
        <Accordion key={`${id}-${index}`} open={index === 0}>
          <AccordionHeading buttonSize="large" colorScheme="secondary">
            <AccordionToggleIcon />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel>
            <Typography>{accordion.content}</Typography>
          </AccordionPanel>
        </Accordion>
      ))}
    </Utility>
  );
};

```

### Multi-select accordion group with disabled accordion
- **Section**: Multi-select accordion groups
- **URL**: components/accordion/multi-select-accordion-group-with-disabled
- **Tags**: 
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
} from '@visa/nova-react';
import { useState } from 'react';

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'multi-select-accordion-group-with-disabled';

const accordions = [
  {
    id: `${id}-panel-1`,
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
    disabled: true,
  },
  {
    id: `${id}-panel-2`,
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    id: `${id}-panel-3`,
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

export const MultiSelectAccordionGroupWithDisabled = () => {
  const [expandedPanels, setExpandedPanels] = useState<{
    [key: string]: boolean;
  }>({
    panel1: false,
    panel2: false,
    panel3: false,
  });

  const handleToggle = (panel: string) => {
    setExpandedPanels(prevState => ({
      ...prevState,
      [panel]: !prevState[panel],
    }));
  };

  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => {
        const panelKey = `panel${index + 1}`;

        return (
          <Accordion id={accordion.id} tag="div" key={accordion.id}>
            <AccordionHeading
              aria-controls={`${accordion.id}-accordion-panel`}
              aria-expanded={expandedPanels[panelKey]}
              disabled={accordion.disabled}
              buttonSize="large"
              colorScheme="secondary"
              id={`${accordion.id}-accordion-header`}
              onClick={() => handleToggle(panelKey)}
              tag="button"
            >
              <AccordionToggleIcon accordionOpen={expandedPanels[panelKey]} />
              {accordion.header}
            </AccordionHeading>
            <AccordionPanel aria-hidden={!expandedPanels[panelKey]} id={`${accordion.id}-accordion-panel`}>
              <Typography>{accordion.content}</Typography>
            </AccordionPanel>
          </Accordion>
        );
      })}
    </Utility>
  );
};

```

### Subtle multi-select accordion group
- **Section**: Multi-select accordion groups
- **URL**: components/accordion/subtle-multi-select-accordion-group
- **Tags**: 
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { CSSProperties } from 'react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'subtle-multi-select-accordion-group';

export const SubtleMultiSelectAccordionGroup = () => {
  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => (
        <Accordion key={`${id}-${index}`}>
          <UtilityFragment vGap={2}>
            <AccordionHeading
              className="v-typography-body-2-medium"
              colorScheme="tertiary"
              style={
                {
                  '--v-accordion-foreground-initial': 'var(--palette-default-active)',
                  '--v-button-default-background': 'transparent',
                } as CSSProperties
              }
            >
              <AccordionToggleIcon />
              {accordion.header}
            </AccordionHeading>
          </UtilityFragment>
          <UtilityFragment vPaddingHorizontal={32}>
            <AccordionPanel
              style={
                {
                  '--v-accordion-panel-background-color': 'transparent',
                  '--v-accordion-panel-border-size': '0px',
                } as CSSProperties
              }
            >
              <Typography>{accordion.content}</Typography>
            </AccordionPanel>
          </UtilityFragment>
        </Accordion>
      ))}
    </Utility>
  );
};

```

### Default single-select accordion group
- **Section**: Single-select accordion groups
- **URL**: components/accordion/default-single-select-accordion-group
- **Tags**: 
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
} from '@visa/nova-react';
import { useState } from 'react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'default-single-select-accordion-group';

export const DefaultSingleSelectAccordionGroup = () => {
  const [openIndex, setOpenIndex] = useState(-1);
  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => (
        <Accordion key={`${id}-${index}`} open={openIndex === index}>
          <AccordionHeading
            buttonSize="large"
            colorScheme="secondary"
            onClick={event => {
              event.preventDefault();
              // If open, close accordion, else open accordion
              setOpenIndex(openIndex === index ? -1 : index);
            }}
          >
            <AccordionToggleIcon />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel>
            <Typography tag="span">{accordion.content}</Typography>
          </AccordionPanel>
        </Accordion>
      ))}
    </Utility>
  );
};

```

### Single-select accordion group with accordion expanded by default
- **Section**: Single-select accordion groups
- **URL**: components/accordion/single-select-accordion-group-with-expanded
- **Tags**: 
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
} from '@visa/nova-react';
import { useState } from 'react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'single-select-accordion-group-with-expanded';

export const SingleSelectAccordionGroupWithExpanded = () => {
  const [openIndex, setOpenIndex] = useState(0);
  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => (
        <Accordion key={`${id}-${index}`} open={openIndex === index}>
          <AccordionHeading
            buttonSize="large"
            colorScheme="secondary"
            onClick={event => {
              event.preventDefault();
              // If open, close accordion, else open accordion
              setOpenIndex(openIndex === index ? -1 : index);
            }}
          >
            <AccordionToggleIcon />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel>
            <Typography tag="span">{accordion.content}</Typography>
          </AccordionPanel>
        </Accordion>
      ))}
    </Utility>
  );
};

```

### Subtle single-select accordion group
- **Section**: Single-select accordion groups
- **URL**: components/accordion/subtle-single-select-accordion-group
- **Tags**: 
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
  UtilityFragment,
} from '@visa/nova-react';
import { CSSProperties, useState } from 'react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'subtle-single-select-accordion-group';

export const SubtleSingleSelectAccordionGroup = () => {
  const [openIndex, setOpenIndex] = useState(-1);
  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => (
        <Accordion key={`${id}-${index}`} open={index === openIndex}>
          <UtilityFragment vGap={2}>
            <AccordionHeading
              className="v-typography-body-2-medium"
              colorScheme="tertiary"
              onClick={event => {
                event.preventDefault();
                // If open, close accordion, else open accordion
                setOpenIndex(openIndex === index ? -1 : index);
              }}
              style={
                {
                  '--v-accordion-foreground-initial': 'var(--palette-default-active)',
                  '--v-button-default-background': 'transparent',
                } as CSSProperties
              }
            >
              <AccordionToggleIcon />
              {accordion.header}
            </AccordionHeading>
          </UtilityFragment>
          <UtilityFragment vPaddingHorizontal={32}>
            <AccordionPanel
              style={
                {
                  '--v-accordion-panel-background-color': 'transparent',
                  '--v-accordion-panel-border-size': '0px',
                } as CSSProperties
              }
            >
              <Typography>{accordion.content}</Typography>
            </AccordionPanel>
          </UtilityFragment>
        </Accordion>
      ))}
    </Utility>
  );
};

```

### Native single-select accordion group
- **Section**: Custom accordion groups
- **URL**: components/accordion/native-single-select-accordion-group
- **Tags**: 
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  Utility,
} from '@visa/nova-react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'native-single-select-accordion-group';

export const NativeSingleSelectAccordionGroup = () => {
  return (
    <Utility vFlex vFlexCol vGap={6}>
      {accordions.map((accordion, index) => (
        <Accordion key={`${id}-${index}`} name={id}>
          <AccordionHeading buttonSize="large" colorScheme="secondary">
            <AccordionToggleIcon />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel>
            <Typography tag="span">{accordion.content}</Typography>
          </AccordionPanel>
        </Accordion>
      ))}
    </Utility>
  );
};

```

### Custom single-select accordion group with accordion expanded by default
- **Section**: Custom accordion groups
- **URL**: components/accordion/default-with-item-open-accordion
- **Tags**: custom
```tsx
import { Fragment } from 'react';
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  useAccordion,
} from '@visa/nova-react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

export const DefaultWithItemOpenAccordion = () => {
  const { isIndexExpanded, toggleIndexExpanded } = useAccordion({ defaultExpanded: 0 });

  return (
    <Accordion id="accordion-default-open-group" tag="div">
      {accordions.map((accordion, index) => (
        <Fragment key={`accordion-default-open-group-${index}`}>
          <AccordionHeading
            aria-controls={`accordion-default-open-panel-${index}`}
            aria-expanded={isIndexExpanded(index)}
            buttonSize="large"
            colorScheme="secondary"
            id={`accordion-default-open-header-${index}`}
            onClick={() => toggleIndexExpanded(index)}
            tag="button"
          >
            <AccordionToggleIcon accordionOpen={isIndexExpanded(index)} />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel aria-hidden={!isIndexExpanded(index)} id={`accordion-default-open-panel-${index}`}>
            <Typography>{accordion.content}</Typography>
          </AccordionPanel>
        </Fragment>
      ))}
    </Accordion>
  );
};

```

### Custom multi-select accordion group with accordion expanded by default
- **Section**: Custom accordion groups
- **URL**: components/accordion/disclosure-group-accordion
- **Tags**: custom
```tsx
import { Fragment } from 'react';
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  useAccordion,
} from '@visa/nova-react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

export const DisclosureGroupAccordion = () => {
  const { isIndexExpanded, toggleIndexExpanded } = useAccordion({ defaultExpanded: [0, 1] });

  return (
    <Accordion id="accordion-disclosure-group" tag="div">
      {accordions.map((accordion, index) => (
        <Fragment key={`accordion-disclosure-group-${index}`}>
          <AccordionHeading
            aria-controls={`accordion-disclosure-group-panel-${index}`}
            aria-expanded={isIndexExpanded(index)}
            buttonSize="large"
            colorScheme="secondary"
            id={`accordion-disclosure-group-header-${index}`}
            onClick={() => toggleIndexExpanded(index)}
            tag="button"
          >
            <AccordionToggleIcon accordionOpen={isIndexExpanded(index)} />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel aria-hidden={!isIndexExpanded(index)} id={`accordion-disclosure-group-panel-${index}`}>
            <Typography>{accordion.content}</Typography>
          </AccordionPanel>
        </Fragment>
      ))}
    </Accordion>
  );
};

```

### Accordion group with arrow key navigation
- **Section**: Custom accordion groups
- **URL**: components/accordion/key-nav-group-accordion
- **Tags**: custom
```tsx
import {
  Accordion,
  AccordionHeading,
  AccordionPanel,
  AccordionToggleIcon,
  Typography,
  useAccordion,
} from '@visa/nova-react';
import { Fragment } from 'react';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 1',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 2',
  },
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Accordion title 3',
  },
];

export const KeyNavGroupAccordion = () => {
  const { isIndexExpanded, onKeyNavigation, ref: accordionRef, toggleIndexExpanded } = useAccordion();

  return (
    <Accordion id="accordion-key-nav-group" onKeyDown={onKeyNavigation} tag="div">
      {accordions.map((accordion, i) => (
        <Fragment key={i}>
          <AccordionHeading
            aria-controls={`accordion-key-nav-group-panel-${i}`}
            aria-expanded={isIndexExpanded(i)}
            buttonSize="large"
            colorScheme="secondary"
            id={`accordion-key-nav-group-header-${i}`}
            onClick={() => toggleIndexExpanded(i)}
            ref={el => {
              accordionRef.current[i] = el;
            }}
            tag="button"
          >
            <AccordionToggleIcon accordionOpen={isIndexExpanded(i)} />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel aria-hidden={!isIndexExpanded(i)} id={`accordion-key-nav-group-panel-${i}`}>
            <Typography>{accordion.content}</Typography>
          </AccordionPanel>
        </Fragment>
      ))}
    </Accordion>
  );
};

```

## Property Sections
### Accordion
- **Selector**: <Accordion />
- **Description**: Sets of vertical headers that reveal or hide the accordion panel.

### AccordionHeading
- **Selector**: <AccordionHeading />
- **Description**: Default summary element, styled as a button that is used to expand and collapse content.

### AccordionPanel
- **Selector**: <AccordionPanel />
- **Description**: Component containing the content of the accordion.

### AccordionToggleIcon
- **Selector**: <AccordionToggleIcon />
- **Description**: Component containing the icon and logic for the accordion toggle icon.

### useAccordion
- **Selector**: None
- **Description**: This hook is used to manage the open state and keyboard navigation of accordions.

## Properties
### ref
- **Section**: Accordion
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: Accordion
- **Type**: ElementType
- **Default**: details
- **Required**: false
- **Description**: Tag of Component

### alternate
- **Section**: AccordionHeading
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Alternate color scheme

### buttonSize
- **Section**: AccordionHeading
- **Type**: "small" , "large"
- **Default**: 
- **Required**: false
- **Description**: Size of Button

### colorScheme
- **Section**: AccordionHeading
- **Type**: "secondary" , "tertiary"
- **Default**: 
- **Required**: false
- **Description**: Color Scheme of Button

### destructive
- **Section**: AccordionHeading
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Destructive Button

### iconButton
- **Section**: AccordionHeading
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Button

### iconTwoColor
- **Section**: AccordionHeading
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Icon Two Button

### ref
- **Section**: AccordionHeading
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### stacked
- **Section**: AccordionHeading
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Stacked Button

### subtle
- **Section**: AccordionHeading
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: Subtle Button

### tag
- **Section**: AccordionHeading
- **Type**: ElementType
- **Default**: summary
- **Required**: false
- **Description**: Tag (not compatible with element property)

### ref
- **Section**: AccordionPanel
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

### tag
- **Section**: AccordionPanel
- **Type**: ElementType
- **Default**: div
- **Required**: false
- **Description**: Tag of Component

### accordionOpen
- **Section**: AccordionToggleIcon
- **Type**: boolean
- **Default**: 
- **Required**: false
- **Description**: manually assign the open state of the accordion

### elementClosed
- **Section**: AccordionToggleIcon
- **Type**: ReactElement
- **Default**: <VisaChevronRightTiny rtl />
- **Required**: false
- **Description**: The icon in closed state

### elementOpen
- **Section**: AccordionToggleIcon
- **Type**: ReactElement
- **Default**: <VisaChevronDownTiny />
- **Required**: false
- **Description**: The icon in the open state

### ref
- **Section**: AccordionToggleIcon
- **Type**: ForwardedRef
- **Default**: 
- **Required**: false
- **Description**: This is a useRef

