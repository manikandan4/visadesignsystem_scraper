# use-accordion

## Metadata
- **Version**: 0.0.1
- **Description**: This hook is used to manage the open state and keyboard navigation of accordions.
- **Category**: hooks

## Example Sections
1. **Behavior and usage**
   - Description: 

## Examples
### 
- **Section**: Behavior and usage
- **URL**: hooks/use-accordion/use-accordion-example
- **Tags**: 
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

// TIP: Customize this ID, pass it as a prop, or auto-generate it with useId() from @react
const id = 'use-accordion-usage';

const accordions = [
  {
    content: 'This is required text that describes the accordion section in more detail.',
    header: 'Section label 1',
  },
];

export const UseAccordionExample = () => {
  // useAccordion hook returns the following:
  // isIndexExpanded: function that returns a boolean value to determine if the accordion is expanded or not
  // onKeyNavigation: function that handles keyboard navigation, and toggles the accordion expanded state
  // ref: a ref object that is used to store the accordion elements
  // toggleIndexExpanded: function that toggles the accordion expanded state, based on the index provided
  const { isIndexExpanded, onKeyNavigation, ref, toggleIndexExpanded } = useAccordion();

  return (
    <Accordion id={id} onKeyDown={onKeyNavigation} tag="div">
      {accordions.map((accordion, i) => (
        <Fragment key={i}>
          <AccordionHeading
            aria-controls={`${id}-panel-${i}`}
            aria-expanded={isIndexExpanded(i)}
            buttonSize="large"
            colorScheme="secondary"
            id={`${id}-header-${i}`}
            onClick={() => toggleIndexExpanded(i)}
            ref={el => {
              ref.current[i] = el;
            }}
            tag="button"
          >
            <AccordionToggleIcon accordionOpen={isIndexExpanded(i)} />
            {accordion.header}
          </AccordionHeading>
          <AccordionPanel aria-hidden={!isIndexExpanded(i)} id={`${id}-panel-${i}`}>
            <Typography tag="span">{accordion.content}</Typography>
          </AccordionPanel>
        </Fragment>
      ))}
    </Accordion>
  );
};

```

