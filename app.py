import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
import time  # Add this import

# ============================================================================
# APP CONFIGURATION (Must be the first command)
# ============================================================================
st.set_page_config(
    page_title="BYU Accounting Study App",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "🏠 Home"

if 'chat_history_402' not in st.session_state:
    st.session_state.chat_history_402 = []


if 'chat_history_405' not in st.session_state:
    st.session_state.chat_history_405 = []

# ============================================================================
# FULL TEXTBOOK CONTENT FOR AI REFERENCE
# ============================================================================
FULL_TEXTBOOK_CONTENT = """
=== COMPLETE TEXTBOOK CONTENT FOR ACC 402 ===

CHAPTER 1: MANAGEMENT ACCOUNTING AND COST MANAGEMENT

Management Accounting and the Role of Cost Management

Management accountants are the accounting and finance professionals who develop and use cost management information to assist in implementing the organization's strategy. Cost management information consists of financial information about costs and revenues and nonfinancial information about customer retention, productivity, quality, and other key success factors for the organization. Cost management is the development and use of cost management information.

The strategic role of the management accountant in an organization is explained in the definition of management accounting provided by the Institute of Management Accountants (IMA):

Management accounting is a profession that involves partnering in management decision making, devising planning and performance management systems, and providing expertise in financial reporting and control to assist management in the formulation and implementation of an organization's strategy.

Management accountants use their unique expertise (decision making, planning, performance management, and more), working with the organization's managers, to help the organization succeed in formulating and implementing its strategy. Cost management information is developed and used within the organization's information value chain, from stage 1 through stage 5.

At lower stages of the value chain, management accountants gather and summarize data (stage 2) from business events (stage 1) and then transform the data into cost management information (stage 3) through analysis and use of the management accountants' expertise. At stage 4, cost management information is combined with other information about the organization's strategy and competitive environment to produce actionable knowledge. At stage 5, management accountants use this knowledge to participate with management teams in making decisions that advance the organization's strategy.

The Four Functions of Management

The management accountant develops cost management information for the CFO, other managers, and employee teams to use to manage the firm and make the firm more competitive and successful. Cost management information is provided for each of the four major management functions:

1. Strategic management
2. Planning and decision making
3. Management and operational control
4. Preparation of financial statements

The most important function is strategic management, which is the development and implementation of a sustainable competitive position in which the firm's competitive advantage provides continued success. A strategy is a set of goals and specific action plans that, if achieved, provide the desired competitive advantage. Strategic management involves identifying and implementing these goals and action plans.

Strategic Management. Cost management information is needed to make sound strategic decisions regarding choice of products, manufacturing methods, marketing techniques and distribution channels, customer profitability, and other long-term issues.

Planning and Decision Making. Cost management information is needed to support recurring decisions regarding replacing equipment, managing cash flow, budgeting materials purchases, scheduling production, and pricing.

Management and Operational Control. Cost management information is needed to provide a fair and effective basis for identifying inefficient operations and to reward and motivate effective managers.

Preparation of Financial Statements. Cost management information is needed to provide accurate accounting for inventory and other assets, in compliance with reporting requirements, for the preparation of financial reports and for use in the three other management functions.

The third area of responsibility, control, consists of two functions, operational control and management control. Operational control takes place when mid-level managers (e.g., site managers, product managers, regional managers) monitor the activities of operating-level managers and employees (e.g., production supervisors and various department heads). In contrast, management control is the evaluation of mid-level managers by upper-level managers (the controller or the CFO).

In the fourth function, preparation of financial statements, management complies with the reporting requirements of relevant groups (such as the Financial Accounting Standards Board) and relevant federal government authorities (e.g., the Internal Revenue Service and the Securities and Exchange Commission).

Strategic Management and the Strategic Emphasis in Cost Management

Effective strategic management is critical to the success of the firm and is a pervasive theme of this book. The growing pressures of economic recession, global competition, technological innovation, and changes in business processes have made cost management more critical and dynamic than ever before. Managers must think competitively; doing so requires a strategy.

Strategic thinking involves anticipating changes; products, services, and operating processes are designed to accommodate expected changes in customer demands. Flexibility is important. The ability to make fast changes is critical as a result of the demands of new concepts such as e-commerce, speed-to-market, and flexible manufacturing.

The strategic emphasis also requires creative and integrative thinking, that is, the ability to identify and solve problems from a cross-functional view. The business functions are often identified as marketing, production, finance, and accounting/controllership. Instead of viewing a problem as a production problem, a marketing problem, or a finance and accounting problem, cross-functional teams view it using an integrative approach that combines skills from all functions simultaneously.

The Contemporary Business Environment

Cost management practices often need to adjust in response to changes in the contemporary business environment. Some of the changes in recent years include:

1. Growth in global competition
2. Lean manufacturing
3. Advances in information technologies and enterprise resource management
4. Continued focus on the customer
5. New forms of management organization
6. Changes in the social, political, and cultural environment of business, including the impact of climate change

The Global Business Environment

A key development that drives change in the contemporary business environment is the growth of international markets and trade due to the rise of economies throughout the world and the decline of trade barriers in many countries.

Lean Manufacturing

To remain competitive in the face of the increased global competition, firms around the world are adopting new manufacturing technologies. These include just-in-time inventory methods to reduce the cost and waste of maintaining large levels of materials and unfinished product. Also, many firms are adopting the lean methods applied in Japanese manufacturing that have produced significant cost and quality improvements through the use of quality teams and statistical quality control.

Use of Information Technology, the Internet, and Enterprise Resource Management

Perhaps the most fundamental of all business changes has been the increasing use of information technology, the internet, and other technologies such as blockchain and artificial intelligence. This new economy is reflected in the rapid growth of internet-based firms; the increased use of the internet for communications, sales, and business data processing; and the use of enterprise management systems.

Focus on the Customer

A key element in the business environment is the need to meet high consumer expectation for product functionality and quality. To meet this expectation, companies have adopted shorter product life cycles, to add new features and new products as quickly as possible, thereby increasing the overall intensity of competition.

Management Organization

Management organization is changing in response to the changes in technology, marketing, and manufacturing processes. Because of the focus on customer satisfaction and value, the emphasis has shifted from financial and profit-based measures of performance to customer-related, nonfinancial performance measures such as quality, time to delivery, and service.

Environmental, Social, and Governance (ESG) Considerations

An additional change to the business environment is an increased concern for how companies manage their relationships with the world in which they operate. Specifically, investors and activist groups are calling on companies to provide regular information about their environmental, social, and governance (ESG) activities.

A company's environmental activities relate to its work to safeguard the environment, including policies to combat climate change. Its social activities relate to how it manages its relationships with employees, customers, and the community at large. Its governance activities relate to issues such as ethical leadership, executive pay, board composition, and shareholder rights.

Contemporary Management Techniques: The Management Accountant's Response to the Contemporary Business Environment

Management accountants, guided by a strategic focus, have responded to the six changes in the contemporary business environment with 13 methods that are useful in implementing strategy in these dynamic times.

The first six methods focus directly on strategy implementation:
1. The balanced scorecard and strategy map
2. Value chain
3. Activity-based costing and management
4. Business analytics
5. Target costing
6. Life-cycle costing

The next seven methods help to achieve strategy implementation through a focus on process improvement:
7. Benchmarking
8. Business process improvement
9. Total quality management
10. Lean accounting
11. The theory of constraints
12. Sustainability
13. Enterprise risk management

The Balanced Scorecard (BSC) and Strategy Map

Strategic information using critical success factors provides a road map for the firm to use to chart its competitive course and serves as a benchmark for competitive success. Financial measures such as profitability reflect only a partial, and frequently only a short-term, measure of the firm's progress.

To emphasize the importance of using strategic information, both financial and nonfinancial, accounting reports of a firm's performance are now often based on critical success factors in four different perspectives:

1. Financial performance. Measures of profitability and market value, among others, as indicators of how well the firm satisfies its owners and shareholders.

2. Customer satisfaction. Measures of quality, service, and low cost, among others, as indicators of how well the firm satisfies its customers.

3. Internal processes. Measures of the efficiency and effectiveness with which the firm produces the product or service.

4. Learning and growth. Measures of the firm's ability to develop and utilize human resources to meet its strategic goals now and into the future.

An accounting report based on the four perspectives is called a balanced scorecard (BSC). The concept of balance captures the intent of broad coverage, financial and nonfinancial, of all factors that contribute to the firm's success in achieving its strategic goals.

The strategy map is a diagram that links the various perspectives in a balanced scorecard. For many companies, high achievement in the learning and growth perspective contributes directly to higher achievement in the internal process perspective, which in turn causes greater achievement in the customer satisfaction perspective, which then produces the desired financial performance.

The Value Chain

The value chain is an analysis tool organizations use to identify the specific steps required to provide a competitive product or service to the customer. In particular, an analysis of the firm's value chain helps management discover which steps or activities are not competitive, where costs can be reduced, or which activity should be outsourced.

A key idea of value-chain analysis is that the firm should carefully study each step in its operations to determine how each step contributes to the firm's profits and competitiveness.

Activity-Based Costing and Management

Many firms have found that they can improve planning, product costing, operational control, and management control by using activity analysis to develop a detailed description of the specific activities performed in the firm's operations. The activity analysis provides the basis for activity-based costing and activity-based management.

Activity-based costing (ABC) is used to improve the accuracy of cost analysis by improving the tracing of costs to products or to individual customers. Activity-based management (ABM) uses activity analysis and activity-based costing to help managers improve the value of products and services and increase the organization's competitiveness.

Business Analytics

Business analytics (BA) (also called predictive analytics) is an approach to strategy implementation in which the management accountant uses data to understand and analyze business performance. Business analytics often uses statistical methods such as regression or correlation analysis to predict consumer behavior, measure customer satisfaction, or develop models for setting prices, among other uses.

Target Costing

Target costing is a method that has resulted directly from the intensely competitive markets in many industries. Target costing determines the desired cost for a product on the basis of a given competitive price, such that the product will earn a desired profit. Cost is thus determined by price.

Life-Cycle Costing

Life-cycle costing is a method used to identify and monitor the costs of a product throughout its life cycle. The life cycle consists of all steps from product design and purchase of materials to delivery and service of the finished product. The steps typically include:

1. Research and development
2. Product design, including prototyping, target costing, and testing
3. Manufacturing, inspecting, packaging, and warehousing
4. Marketing, promotion, and distribution
5. Sales and service

Benchmarking

Benchmarking is a process by which a firm identifies its critical success factors, studies the best practices of other firms (or other business units within a firm) for achieving these critical success factors, and then implements improvements in the firm's processes to match or beat the performance of those competitors.

Business Process Improvement

Business process improvement (BPI) is a management method by which managers and workers commit to a program of continuous improvement in quality and other critical success factors. Continuous improvement is very often associated with benchmarking and total quality management as firms seek to identify other firms as models to learn how to improve their critical success factors.

Total Quality Management

Total quality management (TQM) is a method by which management develops policies and practices to ensure that the firm's products and services exceed customers' expectations. This approach includes increased product functionality, reliability, durability, and serviceability.

Lean Accounting

Firms that have adopted lean manufacturing, which is one of the six key aspects of the contemporary business environment, will also typically use lean accounting. Lean accounting uses value streams to measure the financial benefits of a firm's progress in implementing lean manufacturing.

The Theory of Constraints

The theory of constraints (TOC) is a methodology that improves profitability and cycle time by identifying the bottleneck in the operation and determining the most profitable product mix given the bottleneck. TOC helps to eliminate bottlenecks—places where partially completed products tend to accumulate as they wait to be processed in the production process.

Sustainability

Sustainability means the balancing of the organization's short- and long-term goals in all three dimensions of performance—social, environmental, and financial. We view it in the broad sense to include identifying and implementing ways to reduce cost and increase revenue as well as to maintain compliance with social and environmental regulations and expectations.

Enterprise Risk Management

Enterprise risk management (ERM) is a framework and process that organizations use to manage the risks that could negatively or positively affect the company's competitiveness and success. Risk is considered broadly to include:

1. Hazards such as fire or flood
2. Financial risks due to foreign currency fluctuations, commodity price fluctuations, and changes in interest rates
3. Operating risk related to customers, products, or employees
4. Strategic risk related to top management decisions about the firm's strategy and implementation thereof

===

CHAPTER 3: BASIC COST MANAGEMENT CONCEPTS

Costs, Cost Drivers, Cost Objects, and Cost Assignment

A critical step in achieving a competitive advantage is to identify the key costs and the drivers of those costs within the company or organization.

A company incurs a cost when it uses a resource for some purpose. Often costs are assigned into meaningful groups called cost pools. Costs can be grouped in many different ways, including by type of cost (labor costs in one pool, material costs in another), by source (department 1, department 2), or by responsibility (manager 1, manager 2).

A cost driver is any factor that has the effect of changing the amount of total cost. For a firm that competes on the basis of cost leadership, management of the key cost drivers is essential.

A cost object is any product, service, customer, activity, or organizational unit to which costs are assigned. Products, services, and customers are generally cost objects; manufacturing departments are considered either cost pools or cost objects, depending on whether management's main focus is on the costs for the products or the costs for the manufacturing departments.

Cost Assignment and Cost Allocation: Direct and Indirect Costs

Cost assignment is the process of assigning resource costs to cost pools and then from cost pools to cost objects. There are two types of assignment—direct tracing and allocation.

A direct cost can be conveniently and economically traced directly to a cost pool or a cost object. For example, the cost of materials required for a particular product is a direct cost because it can be traced directly to the product.

While tools like bar code readers and laser scanners allow for significant increases in data collection, for many organizations there is no convenient or economical way to trace an indirect cost from the cost to the cost pool or from the cost pool to the cost object. The cost of supervising manufacturing employees and the cost of handling materials are good examples of costs that generally cannot be easily or economically traced to individual products and therefore are considered indirect costs.

The assignment of indirect costs to cost pools and cost objects is called cost allocation, a form of cost assignment in which direct tracing is not economically feasible, so cost drivers are used instead. The cost drivers used to allocate or assign these costs to cost objects are often called allocation bases.

Direct and Indirect Materials Costs

Direct materials cost includes the cost of materials in the product or other cost object (less purchase discounts but including freight and related charges) and usually a reasonable allowance for scrap and defective units.

On the other hand, the cost of materials used in manufacturing that are not part of the finished product is indirect materials cost. Examples include supplies used by manufacturing employees, such as rags and small tools, or materials required by the machines, such as lubricant.

Direct and Indirect Labor Costs

Direct labor cost includes the labor used to manufacture the product or to provide the service plus some portion of non-value-added time that is normal and unavoidable, such as coffee breaks and personal time.

Indirect labor costs are labor costs associated with production, but are not direct labor. Examples include supervision, quality control, inspection, purchasing and receiving, materials handling, janitorial labor, downtime, training, and cleanup.

Other Indirect Costs

In addition to labor and materials, other types of indirect costs are necessary to manufacture the product or provide the service. They include the costs of facilities, the equipment used to manufacture the product or provide the service, and any other support equipment, such as that used for materials handling.

All indirect costs—for indirect materials, indirect labor, and other indirect items—are commonly combined into a single cost pool called overhead. In a manufacturing firm, it is often called factory overhead.

The three types of costs—direct materials, direct labor, and factory overhead—are sometimes combined for simplicity and convenience. Direct materials and direct labor are sometimes considered together and called prime costs. Similarly, direct labor and overhead are often combined into a single amount called conversion cost.

Cost Drivers and Cost Behavior

Cost drivers provide two important roles for the management accountant: (1) enabling the assignment of costs to cost objects, and (2) explaining cost behavior—that is, the change in the total amount of a cost associated with changes in the level of a cost driver.

The four types of cost drivers are activity-based, volume-based, structural, and executional.

Activity-Based Cost Drivers

Activity-based cost drivers are those factors that cause or contribute to the changes in an activity. The drivers are identified by using activity analysis—a detailed description of the specific activities performed in the firm's operations. The activity analysis includes each step in manufacturing the product or in providing the service. For each activity, a cost driver is determined to explain how the costs incurred for that activity change.

Volume-Based Cost Drivers

Many types of costs are volume-based; that is, the cost driver is the amount produced or quantity of service provided. Management accountants commonly call this volume, or volume of output, or simply output. Good examples of volume-based costs are direct materials cost and hourly direct labor cost—these costs increase with each unit of the volume of output.

The range of the cost driver in which the actual value of the cost driver is expected to fall and for which the relationship to total cost is assumed to be approximately linear is called the relevant range. Outside of this range, the relationship assumed may have to be altered.

Fixed and Variable Costs

Total cost is made up of variable costs and fixed costs. A variable cost is a cost that changes in total in response to changes in one or more cost drivers. While the cost driver can be activity-based or volume-based, typically management accountants in practice use the term variable costs in connection with volume-based cost drivers. A common example of variable costs is the cost of direct materials.

In contrast, a fixed cost is that portion of the total cost that, within the relevant range, does not change with the volume of a designated cost driver. Total fixed costs and unit variable costs are expected to remain approximately constant within the relevant range.

Fixed costs include many indirect costs, especially facility costs (depreciation, rent, insurance, taxes on the plant building), production supervisors' salaries, and other manufacturing support costs that do not change with the number of units produced.

The term mixed cost is used to refer to total cost that, within the relevant range, includes costs for both variable and fixed components.

Step Costs

A cost is said to be a step cost when it varies with the cost driver within the relevant range, but does so in steps. Step costs are characteristic of certain clerical tasks, such as order filling and claims processing.

Unit Cost

Unit cost (or average cost) is the total cost of resources consumed (materials, labor, and overhead) divided by the number of units of output. While average unit cost is a useful concept in setting prices and in evaluating product profitability, it can be subject to some misleading interpretations.

To properly interpret total average unit cost, we must distinguish unit variable costs, which do not change as output changes, from unit fixed costs, which do change as output changes.

Capacity vs. Usage of Costs

It is important to distinguish between costs that provide capacity for operations (e.g., plant building and equipment) and costs that are consumed during operations (e.g., direct materials). The former are fixed costs, while the latter are variable costs.

Structural and Executional Cost Drivers

Structural and executional cost drivers are used to facilitate strategic decision making. Structural cost drivers are strategic in nature because they involve decisions that have long-term effects on the firm's total costs.

Four examples of decisions involving structural cost drivers:

1. Scale. Larger firms have lower overall costs as a result of economies of scale.

2. Experience. Firms having employees with greater manufacturing and sales experience will likely have lower development, manufacturing, and distribution costs.

3. Technology. New technologies can reduce design, manufacturing, distribution, and customer service costs significantly.

4. Complexity. How many different products does the firm have? Firms with many products have higher costs of scheduling and managing the production process, as well as the upstream costs of product development and the downstream costs of distribution and service.

Executional cost drivers are factors the firm can manage in short-term, operational decision making to reduce costs. Here are three examples of executional cost drivers:

1. Workforce empowerment. Are the employees dedicated to continual improvement and quality? This workforce commitment will lower costs.

2. Design of the production process. Is the production process efficient? Speeding up the flow of product through the firm can reduce costs.

3. Supplier relationships. Can the cost, quality, or delivery of materials and purchased parts be improved to reduce overall costs?

Cost Concepts for Product and Service Costing

Accurate information about the cost of products and services is important in each management function: strategic management, planning and decision making, management and operational control, and financial statement preparation.

Product Costs and Period Costs

Product inventory for both manufacturing and merchandising firms is treated as an asset on their balance sheets. As long as the inventory has market value, it is considered an asset until the inventory is sold; then the cost of the inventory is transferred to the income statement as cost of goods sold.

Product costs for a manufacturing firm include only the costs necessary to complete the product at the manufacturing step in the value chain:

1. Direct materials. The materials used to manufacture the product, which become a physical part of it.

2. Direct labor. The labor used to manufacture the product.

3. Factory overhead. The indirect costs for materials, labor, and facilities used to support the manufacturing process.

Product costs for a merchandising firm include the cost to purchase the product plus the transportation costs paid by the retailer or wholesaler to get the product to the location from which it will be sold or distributed.

All other costs for managing the firm and selling the product are not product costs. They are expensed in the period in which they are incurred; for that reason, they are also called period costs. Period costs (nonproduct costs) include the selling, general, and administrative costs that are necessary for the management of the company but are not involved directly or indirectly in the manufacturing process (or, for a retailer, in the purchase of the products for resale).

Manufacturing and Merchandising Costing

The cost flows in manufacturing, retail, and service firms differ. Manufacturing companies use three inventory accounts:

1. Materials Inventory, which contains the cost of the supply of materials to be used in the manufacturing process

2. Work-in-Process Inventory, which contains all costs put into the manufacture of products that are started but not complete at the financial statement date

3. Finished Goods Inventory, which contains the cost of goods that are ready for sale

An inventory formula relates the inventory accounts, as follows:

Beginning inventory + Cost added = Cost transferred out + Ending inventory

The terms cost added and cost transferred out have different meanings, depending on which inventory account is being considered:

Materials Inventory:
- Cost added: Purchase of materials
- Cost transferred out: Cost of materials used in production

Work-in-Process Inventory:
- Cost added: (1) Cost of direct materials used, (2) Direct labor cost, (3) Overhead cost
- Cost transferred out: Cost of goods manufactured

Finished Goods Inventory:
- Cost added: Cost of goods manufactured
- Cost transferred out: Cost of goods sold

Key Formulas:

Prime Costs = Direct Materials + Direct Labor
Conversion Costs = Direct Labor + Factory Overhead
Total Product Cost = Direct Materials + Direct Labor + Factory Overhead
Cost of Goods Manufactured = Beginning WIP + Manufacturing Costs - Ending WIP
Cost of Goods Sold = Beginning FG + COGM - Ending FG

===

CHAPTER 4: JOB COSTING

Costing Systems

Costing is the process of accumulating, classifying, and assigning direct materials, direct labor, and factory overhead costs to cost objects, which most commonly are products, services, or projects.

In developing the particular costing system to fit a specific firm, the management accountant must make three choices, one for each of the three following characteristics of costing methods:

1. The cost accumulation method—job costing or process costing
2. The cost measurement method—actual, normal, or standard costing
3. The overhead application method—volume-based or activity-based

Cost Accumulation: Job or Process Costing?

Costs can be accumulated by tracing costs to a specific product or service or by accumulating costs at the department level and then allocating these costs from the departments to the products or services.

In a job costing system, the jobs consist of individual products or batches of products or services. A job costing system is appropriate when most costs incurred for the job can be readily identified with a specific product, batch of products, customer order, contract, or project.

In contrast, process costing is likely to be found in a firm that primarily produces homogeneous products or services. These firms often have continuous mass production. In this case, it is economically impractical to trace most costs to individual products.

Cost Measurement: Actual, Normal, or Standard Costing?

An actual costing system uses actual costs incurred for all product costs, including direct materials, direct labor, and factory overhead.

A normal costing system uses actual costs for direct materials and direct labor, and normal costs for factory overhead. Normal costing involves estimating a portion of overhead to be assigned to each product as it is produced.

A standard costing system uses standard costs and quantities for all three types of manufacturing costs: direct materials, direct labor, and factory overhead. Standard costs are expected costs the firm should attain.

Overhead Application under Normal Costing: Volume-Based or Activity-Based?

Volume-based product costing systems allocate overhead to products or jobs using only volume-based cost drivers, such as units produced.

Activity-based costing (ABC) systems allocate factory overhead costs to products using cause-and-effect criteria with multiple cost drivers. ABC systems use both volume-based and non-volume-based cost drivers to more accurately allocate factory overhead costs to products based on resource consumption during various activities.

The Strategic Role of Costing

To compete successfully, firms need accurate cost information, regardless of their competitive strategies. This is even more likely to be true for cost leadership firms that rely on a high level of manufacturing efficiency and quality to succeed.

Job Costing: The Cost Flows

Job costing is a costing system that accumulates costs and assigns them to specific jobs, customers, projects, or contracts. The basic supporting document (usually in electronic form) in a job costing system is the job cost sheet. It records and summarizes the costs of direct materials, direct labor, and factory overhead for a particular job.

Direct and Indirect Materials Costs

As part of the preparation for the job, the firm purchases materials that are needed for the job. These purchases include both direct materials (lumber, fabric, and other direct materials) and indirect materials (glue, nails, and other indirect materials).

The purchase of materials is based off the production levels and the bill of materials for each product. The bill of materials is a detailed listing of all the materials needed for a given job.

Once production is to begin, the various production departments will refer to the bill of materials for the job and then use a materials requisition to request the materials needed for production. The materials requisition indicates the specific job charged with the materials used.

Direct and Indirect Labor Costs

Direct labor costs are recorded on the job cost sheet by means of a time ticket (an online data entry or source document) prepared for each employee. A time ticket shows the amount of time an employee worked on each job, the pay rate, and the total direct labor cost chargeable to each job.

Indirect labor costs are treated as part of the total factory overhead cost. Indirect labor includes items such as salaries or wages for supervisors, inspectors, and production warehouse clerks.

Factory Overhead Costs

Overhead application is a process of allocating factory overhead costs to cost objects. In this chapter, the cost objects are jobs. Allocation is necessary because overhead costs are not traceable to individual jobs.

Actual Costing

An actual costing system uses actual costs incurred for direct materials and direct labor and records actual factory overhead for the jobs.

Generally, the total amount of actual overhead costs is not known until the end of the accounting period when total expenses are determined. Thus, in an actual costing system, all job costs are recorded at the end of the accounting period.

Normal Costing

In practice, many firms adopt a normal costing system that uses actual costs for direct materials and direct labor and applies factory overhead to jobs by adding to the job an estimated amount of overhead in the job by using a predetermined rate.

Normal costing avoids the fluctuations in cost per unit under actual costing resulting from changes in the month-to-month volume of units produced and changes in overhead costs from month to month.

The Application of Factory Overhead in Normal Costing

The predetermined factory overhead rate is an estimated rate used to apply factory overhead cost to a specific cost object or job. The amount of overhead applied to a job using a predetermined factory overhead rate is called factory overhead applied.

The predetermined overhead rate is calculated from estimates of overhead costs and cost drivers for the upcoming operating period, usually the coming fiscal year. To obtain the predetermined overhead rate, use these four steps:

1. Estimate total factory overhead costs for the planned production for the upcoming operating period, usually a year.

2. Select the most appropriate cost driver(s) for applying the factory overhead costs.

3. Estimate the total amount of the chosen cost driver(s) for the upcoming operating period.

4. Divide the estimated factory overhead costs by the estimated amount of the chosen cost driver(s) to obtain the predetermined overhead rate.

Cost Drivers for Factory Overhead Application

The cost driver selected for applying a predetermined overhead rate can be either a volume- or activity-based cost driver. Direct labor hours, direct labor costs, and machine-hours are among the most frequently used volume-based cost drivers for applying factory overhead.

Applying Factory Overhead Costs

The predetermined overhead rate usually is calculated at the beginning of the year and is used throughout the year.

Predetermined factory overhead rate = Estimated total factory overhead amount for the year / Estimated total amount of cost driver for the year

Departmental Overhead Rates

When the production departments in the plant are very similar as to the amount of overhead in each department and the usage of cost drivers in the departments, then the use of a plantwide rate (one rate for all production departments taken as a whole) is appropriate.

In many cases, however, the various production departments differ significantly in the amount of cost or cost drivers. Using a departmental allocation approach, the rates are calculated separately for each department, and the overhead is allocated to products based on the usage of each department's resources.

Disposition of Underapplied and Overapplied Overhead

Using a predetermined factory overhead rate to apply overhead cost to products can cause total overhead applied to the units produced to exceed the actual overhead incurred in periods when production is higher than expected.

Overapplied overhead is the amount of factory overhead applied that exceeds the actual factory overhead cost incurred.

On the other hand, it is possible that applied overhead will be less than the incurred amount of overhead. Underapplied overhead is the amount by which actual factory overhead exceeds factory overhead applied.

Underapplied or overapplied overhead can be disposed of in two ways:

1. Adjust the Cost of Goods Sold account.

2. Adjust the production costs of the period; that is, allocate (often called "prorate") the underapplied or overapplied overhead among the ending balances of Work-in-Process Inventory, Finished Goods Inventory, and Cost of Goods Sold.

Adjustment to Cost of Goods Sold

When the amount of underapplied or overapplied overhead is not significant, it generally is adjusted to Cost of Goods Sold because all product costs eventually become cost of goods sold.

Proration Approach

If management believes the amount of overapplied or underapplied overhead represents a material amount, then proration of the amount to Work-in-Process Inventory, Finished Goods Inventory, and Cost of Goods Sold is the preferred method of disposal.

Potential Errors in Overhead Application

The application of overhead is a critical step in costing, and because it is based on estimates, it is subject to potential errors in determining the cost of a product or service. There are three types of potential errors:

1. Aggregation error. This costing error arises when, for example, a single plantwide rate is used instead of departmental rates.

2. Specification error. This error arises when the wrong cost driver is used in the application rate.

3. Measurement error. This is a common type of error that arises when the amounts used for estimated cost drivers or estimated overhead are incorrect.

Job Costing in Service Industries; Project Costing

Job costing is used extensively in service industries such as advertising agencies, hospitals, and repair shops, as well as consulting, architecture, accounting, and law firms. Instead of using the term job, accounting and consulting firms use the term client or project, hospitals and law firms use the term case, and advertising agencies use the term contract or project. Many firms use the term project costing to indicate the use of job costing in service industries.

Operation Costing

Operation costing is a hybrid costing system that uses a job costing approach to assign direct materials costs to jobs and a process costing approach to assign conversion costs to products or services.

Manufacturing operations whose conversion activities are very similar across several product lines, but whose direct materials used in the various products differ significantly, use operation costing.

Industries suitable for applying operation costing include food processing, textiles, shoes, furniture, metalworking, jewelry, and electronic equipment.

===

CHAPTER 6: PROCESS COSTING

Characteristics of Process Costing Systems

Firms having homogeneous products that pass through a series of similar processes or departments use process costing. These firms usually engage in continuous mass production of a few similar products. Manufacturing costs are accumulated in each process.

The process costing system is used in many industries such as chemicals, oil refining, textiles, paints, flour, canning, rubber, steel, glass, food processing, mining, electronics, plastics, drugs, paper, lumber, leather goods, metal products, and sporting goods.

Equivalent Units

An equivalent unit is the measure commonly used in process costing. Equivalent units are the number of the same or similar complete units that could have been produced given the amount of work actually performed on both complete and partially complete units.

Equivalent units are not the same as physical units. For example, suppose in a given month a chemical company had 30,000 gallons of a chemical in production, of which 20,000 gallons were complete at the end of the month but the remaining 10,000 gallons were only 50% complete. The equivalent units would be 25,000 gallons [20,000 + (10,000 × 50%)].

The equivalent units should be calculated separately for direct materials, direct labor, and factory overhead when the proportion of the total work performed on the units in the Work-in-Process Inventories is not always the same for each cost element.

Conversion Costs

Because overhead is often applied on the basis of direct labor hours, and because of the relatively small direct labor content in most process industries, factory overhead and direct labor costs are often combined and called conversion costs for the purpose of computing equivalent units of production.

Many manufacturing operations incur conversion costs uniformly throughout production. The equivalent units of conversion costs are therefore the result of multiplying the percentage of work that is complete during the period by the number of units on which work is partially complete.

Direct Materials

Direct materials can be added at discrete points or continuously during production. If the materials are added uniformly, the proportion used for computing equivalent units of direct materials is the same as the proportion for conversion costs, and a separate calculation of the direct materials per equivalent would not be necessary.

However, if the materials are added all at once, the proportion used in the computation depends on whether the point in the process where the materials are added has been reached.

Flow of Costs in Process Costing

In process costing, costs flow through different processes or departments. A separate Work-in-Process Inventory account is used to record costs of each production department.

When one department finishes its work, the costs of the goods completed are transferred to the next department's Work-in-Process Inventory account for further work. After this further work, the costs of goods completed are then transferred to the Finished Goods Inventory account.

Starting with the second department, an additional cost element, transferred-in costs, appears. These are costs of the goods completed in the prior department and transferred into this department during the period.

Steps in Process Costing (The Production Cost Report)

The key document in a typical process costing system is the production cost report, prepared at the end of each period for each production process or department. The production cost report summarizes the number of physical units and equivalent units of a department, the costs incurred during the period, and the costs assigned to both units completed (and transferred out) and ending Work-in-Process Inventories.

The preparation of a production cost report includes five steps:

Step 1: Analyze the physical flow of production units.

Step 2: Calculate equivalent units for each manufacturing cost element (direct materials, direct labor, and overhead or direct materials and conversion costs).

Step 3: Determine total costs for each manufacturing cost element from step 2.

Step 4: Compute cost per equivalent unit for each manufacturing cost element from step 2.

Step 5: Assign total manufacturing costs to units completed and ending Work-in-Process (WIP).

Step 1: Analyze the Physical Flow of Production Units

The first step determines the number of units on hand in beginning Work-in-Process, the number of units started into production (or received from a prior department), the number of units completed, and the number of units in ending Work-in-Process Inventory.

Input units include beginning Work-in-Process Inventory and all units that enter a production department during an accounting period. Output units include units that are complete and transferred out from a production department and units in the ending Work-in-Process Inventory.

Step 2: Calculate Equivalent Units for Each Manufacturing Cost Element

The purpose of calculating equivalent units of production for each manufacturing cost element (direct materials, direct labor, and factory overhead) is to measure the total work expended on production during an accounting period. The partially complete physical units are converted into the equivalent number of whole units.

Step 3: Determine Total Costs for Each Manufacturing Cost Element

The total manufacturing costs for each cost element (direct materials, direct labor, and overhead) include the current costs incurred and the prior period costs of the units in Work-in-Process beginning inventory. The total manufacturing cost for each cost element is also called total costs to account for.

Step 4: Compute Cost per Equivalent Unit for Each Manufacturing Cost Element

The purpose of computing cost per equivalent unit of production is to have a proper product costing for income determination and other management needs for an accounting period, which includes both complete and incomplete units.

Step 5: Assign Total Manufacturing Costs to Units Completed and Ending WIP

The objective of the production cost report is to assign total manufacturing costs incurred to the units completed during the period and the units that are still in process at the end of the period. The total costs assigned in step 5 should equal the total costs to be accounted for in step 3.

Process Costing Methods

The two methods used to prepare the departmental production cost report when the firm uses process costing are the weighted-average method and the first-in, first-out (FIFO) method.

Weighted-Average Method

The weighted-average method includes all costs in calculating the unit cost, including both costs incurred during the current period and costs incurred in the prior period that are shown as the beginning Work-in-Process Inventory of the current period. In this method, prior period costs and current period costs are averaged—hence the name, weighted-average.

The weighted-average method makes no distinction between the cost incurred prior to the current period and the cost incurred during the current period. As long as a cost is on the current period's cost sheet for a production department, it is treated as any other cost regardless of when it was incurred.

The weighted-average method computes the total equivalent units produced to date. The number of units in production in the current period for each manufacturing production element includes both (1) the units from previous periods that are still in production at the beginning of the current period and (2) the units placed into production in the current period.

Total equivalent units = Completed and transferred out units + Ending Work-in-Process equivalent units

FIFO Method

The FIFO method includes only costs incurred and work performed during the current period in calculating the unit cost. FIFO considers the beginning inventory as a batch of goods separate from the goods started and completed within the current period. FIFO assumes that the first work done is to complete the beginning Work-in-Process Inventory.

The FIFO method does not combine beginning inventory costs with current costs when computing equivalent unit costs. While the costs from each period are treated separately, we still follow the same five steps as in the weighted-average method in determining product costs.

The equivalent units in the beginning Work-in-Process—work done in the prior period—are not counted as part of the FIFO method equivalent units. Only the equivalent units of the beginning Work-in-Process to be completed this period are counted.

FIFO equivalent units = Completed and transferred out units + Ending Work-in-Process equivalent units - Beginning Work-in-Process equivalent units

Comparison of Weighted-Average and FIFO Methods

Both the weighted-average and the FIFO methods produce the same total costs accounted for. The key difference between the two methods is the handling of partially completed beginning Work-in-Process Inventory units.

The FIFO method separates the units in the beginning inventory from the units started and completed during the period. In contrast, the weighted-average method makes no separate treatment of the units in the beginning Work-in-Process Inventory.

The weighted-average method generally is easier to use because the calculations are simpler. This method is most appropriate when Work-in-Process Inventory is relatively small or when direct materials prices and conversion costs are stable.

The FIFO method is most appropriate when direct materials prices, conversion costs, or inventory levels fluctuate significantly.

Some firms prefer the FIFO method over the weighted-average method for purposes of cost control and performance evaluation because the cost per equivalent unit under FIFO represents the cost for the current period's efforts only.

Process Costing with Multiple Departments

Most manufacturing firms have multiple departments or use several processes that require a number of steps. As the product passes from one department to another, the cost passes from department to department. The costs from the prior department are called transferred-in costs or prior department costs.

Transferred-in Costs

Transferred-in costs are costs of work performed in the earlier departments that are transferred into the present department. Including these costs is a necessary part of process costing because we treat each department as a separate entity, and each department's production cost report includes all costs added to the product up to that point.

The equivalent units of the transferred-in cost for ending Work-in-Process Inventory is always assumed to be the same as the number of units in ending Work-in-Process Inventory. Because all units in process are complete for the prior departments' costs, by definition the number of equivalent units transferred in is the same as the number of physical units transferred in.

Journal Entries for Process Costing

Process costing uses the same general ledger manufacturing accounts as job costing. However, instead of assigning product costs to specific jobs, we accumulate costs in production departments. Each department has a separate Work-in-Process Inventory account.

Implementation and Enhancement of Process Costing

Activity-Based Costing and the Theory of Constraints

Process costing systems are appropriate where there are one or a few homogeneous products. But sometimes the process-based manufacturer has very different products going through different processes, making the process costing system by itself inadequate.

Activity-based costing is an important enhancement to process costing when product and process variety arises. Similarly, process costing information is not intended to help the firm determine the most profitable product mix or to identify the most profitable use of the plant. These questions require analyses that utilize the products' contribution margins and the location of production constraints in the plant.

Just-in-Time Systems and Backflush Costing

Firms use the just-in-time (JIT) method to minimize inventory and improve quality by carefully coordinating the receipt of materials and the delivery of products with the manufacturing processes in the plant. The goal is to have little or no Direct Materials, Work-in-Process, or Finished Goods Inventory in the plant.

Because inventory is minimal in an effective JIT system, there is no need for a system such as process costing to determine equivalent units and to account for production costs in Work-in-Process and Finished Goods. Simpler methods such as backflush costing can be used instead.

Backflush costing charges current production costs (using standard unit costs) directly to finished goods inventory, without accounting for the flows in and out of the Work-in-Process account, or directly to Cost of Goods Sold without accounting for the flows in and out of WIP or Finished Goods.

Normal and Standard Process Costing

Process cost reports can take a normal costing approach; that is, direct labor and direct materials are added to product at actual cost and overhead is determined and applied to product using a predetermined overhead rate. An alternative approach is standard costing, in which all three cost elements—direct materials, direct labor, and overhead—are added to product at a standard cost rather than actual cost.

Both job costing and process costing can be applied using either the normal costing or the standard costing approach. Similarly, a process costing system can be either a traditional or an activity-based system.

===

CHAPTER 7: COST ALLOCATION: DEPARTMENTS, JOINT PRODUCTS, AND BY-PRODUCTS

The Strategic Role and Objectives of Cost Allocation

The strategic role of cost allocation has four objectives:

1. Determine accurate departmental and product costs as a basis for the evaluation of the cost efficiency of departments and the profitability of different products, financial reporting, and tax compliance.

2. Motivate managers to exert a high level of effort to achieve the goals of top management.

3. Provide the right incentive for managers to make decisions that are consistent with the goals of top management.

4. Fairly determine the rewards earned by the managers for their effort and skill and for the effectiveness of their decision making.

The first and most important objective requires the cost allocation method to be sufficiently accurate to support effective management decision making about products and departments. The cost allocation methods must also comply with the financial reporting standards of the Financial Accounting Standards Board (FASB) and the Internal Revenue Service.

The second objective, motivating managers, means that to be effective, the cost allocation (when it is later used as part of performance evaluation and compensation) must reward department managers for reducing costs as desired.

The third objective, providing the incentive for decision making, is achieved when cost allocation effectively provides the incentives for the individual manager to act autonomously in a manner that is consistent with top management's goals.

The fourth objective, fairness, is met when the cost allocation is clear and consistently applied in determining the manager's performance evaluation and compensation. The most clear and unbiased basis for cost allocation exists when a cause-and-effect relationship can be determined.

In some situations, cause-and-effect bases are not available and alternative concepts of fairness are used. One such concept is ability-to-bear, which is commonly employed with bases related to size, such as total sales, total assets, or the profitability of the user departments. Other concepts of fairness are based on equity perceived in the circumstance, such as benefit received.

The Ethical Issues of Cost Allocation

A number of ethical issues are important in cost allocation:

1. Ethical issues arise when costs are allocated to products or services that are produced for both a competitive market and a public agency or government department.

2. A second ethical issue in implementing cost allocation methods is the equity or fair share issue that arises when a governmental unit reimburses the costs of a private institution or when it provides a service for a fee to the public.

3. A third important ethical issue is the effect of the chosen allocation method on the costs of products or services sold to or from foreign subsidiaries.

Cost Allocation to Service and Production Departments

The departmental cost allocation method has three phases (or "steps"):

Phase 1: Trace, rather than allocate, all direct manufacturing costs and allocate manufacturing overhead costs to both the service departments and the production departments

Phase 2: Allocate the service department costs to the production departments

Phase 3: Allocate the production department costs to the products

First Phase: Trace Direct Costs and Allocate Indirect Costs to All Departments

The first phase in the departmental allocation approach traces the direct costs and allocates the indirect manufacturing costs in the plant to each service and production department.

Direct manufacturing costs are wages and materials that can be directly linked or traced to a department; for example, direct materials and direct labor costs would be traced to the production departments where they are used. Indirect costs, such as indirect materials, indirect labor, and other costs that cannot be easily and economically traced to a department are allocated by means of a predetermined cost driver to the departments that use those resources.

Allocation in Second and Third Phases

The second phase allocates service department costs to the production departments. This is the most complex of the allocation phases because services can flow back and forth between the service departments. These are often called reciprocal flows, which represent the flow of services back and forth between service departments.

Management accountants can choose among three common methods to allocate costs for the second phase:
1. The direct method
2. The step method
3. The reciprocal method

The Direct Method

The direct method of departmental cost allocation is the simplest of the three methods because it ignores the reciprocal flows. The cost allocation is accomplished by using the service flows only to production departments and determining each production department's share of that service.

The Step Method

The second method to allocate service department costs is the step method, so-called because it uses a sequence of steps in allocating service department costs to production departments. In the first step, one service department is selected to be allocated fully, that is, to allocate its costs to the other service departments as well as to each production department.

The department to be allocated first usually is chosen because it provides the highest percentage of service to other service departments. Overall, this means that the step method may provide more accurate allocations because one of the reciprocal flows between the two service departments (the one in the first step) is considered in the allocation—unlike the direct method, which ignores all reciprocal flows.

The Reciprocal Method

The reciprocal method is the preferred of the three methods because, unlike the others, it considers all reciprocal flows among the service departments. This is accomplished by using simultaneous equations; the reciprocal flows are simultaneously determined in a system of equations.

An equation for each service department represents the cost to be allocated, consisting of the first-phase allocation costs plus the cost allocated from the other department.

Implementation Issues

The key implementation issue is the choice of the most accurate allocation method. When significant differences exist, a management accountant should consider the value of the reciprocal method, which is more complete and accurate than the others because it fully considers the reciprocal flows between service departments.

Three additional issues to consider when implementing the departmental allocation approach are:

1. Disincentive effects when the allocation base is unrelated to usage
2. Disincentive effects when the allocation base is actual usage
3. Disincentive effects when allocated costs exceed external purchase cost

Disincentive Effects When the Allocation Base Is Unrelated to Usage

Determining an appropriate allocation base and the percentage amount for service provided by the service departments is often difficult. Using an inappropriate allocation base can have undesirable motivational consequences.

Disincentive Effects When the Allocation Base Is Actual Usage

When the cost allocation base is determined from actual usage, disincentives can arise because the usage of the resource by one department will affect the cost allocation to other departments.

Dual Allocation

The disincentives can be resolved by using dual allocation. Dual allocation separates fixed and variable costs and traces variable costs to the departments based on actual usage; fixed costs are allocated based on either an equal share among departments or a predetermined budgeted proportion.

The reason for the equal-share approach is that each department pays in effect a fee for the right to receive future services from the service department, irrespective of the amount of service to be used. This concept is similar to the minimum monthly charge on a checking account or for a utility bill.

Disincentive Effects When Allocated Costs Exceed External Purchase Cost

Another limitation of the three departmental allocation methods is that sometimes they can allocate a higher cost for the service than the department would pay were it to purchase the service from an outside supplier. To motivate managers to be efficient and for fairness, the allocation should be based on the cost of obtaining the service outside the firm.

Cost Allocation in Service Industries

The concepts presented in this chapter apply equally well to manufacturing, service, or not-for-profit organizations that incur joint costs. Financial institutions such as commercial banks also use cost allocation.

A service department is a unit of the organization that performs one or more support tasks for production departments by supplying engineering services, information technology, quality control, human resources management, or some other service to the production departments. The production departments assemble and finish the products.

The service department costs are allocated to the production departments, and then the costs of the production departments are allocated to the products.

Joint Product Costing

Many manufacturing plants yield more than one product from a joint manufacturing process. A joint production process is one that yields multiple outputs from a common resource input.

Joint products are products from a joint production process that have relatively substantial sales values. Products whose total sales values are minor in comparison to the sales value of the joint products are classified as by-products.

The point in a joint production process at which individual products can be separately identified for the first time is called the split-off point. Thereafter, separate production processes can be applied to the individual products.

Joint costs include all manufacturing costs incurred prior to the split-off point (including direct materials, direct labor, and factory overhead). For financial reporting purposes, these costs are allocated among the joint products.

Additional costs incurred after the split-off point that can be identified directly with individual products are called separable processing costs.

Methods for Allocating Joint Costs to Joint Products

Joint costs are most frequently allocated to joint products using:
1. The physical measure
2. The sales value at split-off
3. The net realizable value
4. The constant gross margin percentage methods

The Physical Measure Method

The physical measure method uses a physical measure such as pounds, gallons, yards, or units produced at the split-off point to allocate the joint costs to joint products.

Advantages and Limitations:
- Advantages: (1) It is easy to use and (2) the criterion for the allocation of the joint costs is objective.
- Limitations: This method ignores the revenue-producing capability of individual products that can vary widely among the joint products and have no relationship at all to any physical measure.

The Sales Value at Split-Off Method

The sales value at split-off method (or, more simply, relative sales value method) allocates joint costs to joint products on the basis of their relative sales values at the split-off point. This method can be used only when joint products can be sold at the split-off point.

Advantages and Limitations:
- Advantages: (1) It is easy to calculate and (2) is allocated according to each product's revenues. This method is superior to the physical measure method because it allocates the joint costs in proportion to the products' ability to absorb these costs.
- Limitations: One limitation is that market prices for some industries change constantly. Also, the sales price at split-off might not be available because separable processing is necessary before the product can be sold.

The Net Realizable Value Method

Not all joint products can be sold at the split-off point; some require additional processing before the product can be sold. Thus, there is no market price to attach to some products at the split-off point. In these cases, the concept of net realizable value is used.

The net realizable value (NRV) of a product is the ultimate net sales value that is estimated at the split-off point; it is determined by subtracting the separable processing and selling costs beyond the split-off point from the estimated ultimate sales value for that product.

NRV = Estimated ultimate sales value - Separable processing and selling costs

Advantages and Limitations:
The NRV method is superior to the physical measure method because, like the sales value at split-off method, it produces an allocation that yields a predictable, comparable level of profitability among the products.

The Decision to Sell before or after Additional Processing:
An important decision for management to make in regard to separable costs is whether the company should incur the separable costs and process the product further. The key to making this decision is to ignore the joint costs and focus instead on only the separable costs and the increase in sales value.

The joint costs are not relevant for the decision because these costs will not differ between the option to sell at the split-off point or to sell after additional processing.

The Constant Gross Margin Percentage Method

Sometimes it is desirable that the company has joint products with constant or equal gross margin percentages. The constant gross margin percentage method determines an allocation of joint costs so that, after allocation, all joint products have the same gross margin percentage.

The method for achieving constant gross margin percentages for joint products involves:
1. Summarizing basic data
2. Determining gross margin percent for total sales
3. Allocating joint cost and determining total product cost
4. Calculating gross margin

===


PROCESS COSTING LECTURE NOTES (SUPPLEMENTAL)

PROCESS COSTING, PART 1

As you recall from earlier in the semester, job-order costing is used for assigning costs to jobs or units that we can individually distinguish and manage. With job-order costing, costs are assigned to specific units. When a job is completed, the costs associated with that job move from the Work in Process Inventory account to the Finished Goods Inventory account.

Process costing is a method of assigning costs to products, similar to job-order costing. Process costing is used for assigning costs to jobs or units that are not individually distinguishable (e.g., identical products that are mass produced). Because jobs are indistinguishable, it really isn't possible to assign costs to specific units as is done with job order costing. Instead, we assign costs to departments and then calculate an average cost per unit for each department for a given time period. We then take the number of units that move out of a given department in a given time period and multiply that by the average cost per unit to determine the cost transferred out of the department each period.

Equivalent Units

Getting an average cost per unit in process costing requires two components: the total cost for the department in a given period (the numerator), and the total number of units made in the department in a given period (the denominator). Conceptually, this is fairly straightforward. For example, if total costs assigned to a given department in a given time period are $1,000, and total units made during that time period in that department are 100, we would have:

Average Cost per Unit = Total Costs / Total Units = $1,000 / 100 units = $10

Calculation of the numerator (the total cost incurred for a department in a given period) involves directly tracing costs (direct labor and direct materials) and allocating overhead (e.g., via a traditional costing system or activity-based costing) to a department for a specific time period.

Calculation of the denominator (the total number of units made in the department in a given period) is complicated by the fact that some units are started and completed in a given period, some units are started but not completed in a given period, and some units that were started last period are completed this period. One approach to calculating the "total units made" is to simply add up all the units we worked on in a given period. Let's think about the implications of using this approach.

First, recall that with process costing we are trying to determine the costs that get transferred out of a department when a unit is transferred out of the department. This is the purpose of calculating the average cost per unit. We will multiply the cost per unit by the number of units transferred out to get the costs transferred out. If we use the total units worked on in calculating our average cost per unit, we are implicitly assuming that each unit received the same amount of work, or, in other words, we are assuming that each unit incurred the same costs. But surely the units we started and completed this period incurred more costs than units we started but did not complete.

To address this problem, we use the concept of "equivalent units." Equivalent units expresses some number of incomplete units as a smaller number of completed units. One way of thinking about the number of equivalent units is that the company could have produced this number of completed units, given the amount of costs incurred. For example, if we have 100 units that are 30% complete (on average), we would have made 30 "equivalent units."

Using equivalent units, we can now express the number of units made this period in a way that accounts for the fact that we didn't do the same amount of work on each unit. We can now divide the total cost for a department this period by the total number of equivalent units "done" or "made" this period to get a cost per equivalent unit for the department for the period. For example, if total costs assigned to a given department in a given time period are $1,000, and total equivalent units are 50, we have:

Average Cost per Equivalent Unit (EU) = Total Costs / Total EU = $1,000 / 50 EU = $20

Because a completed unit is equal to one equivalent unit (since it is 100% complete), we can now multiply the cost per equivalent unit by the number of physical units transferred out of the department to determine the cost that should be transferred out of the department. For example, if we transferred out 10 units, we would have:

Costs transferred out = Cost per EU × # of units transferred out = $20 × 10 = $200

Tracking Cost Types Separately

Not all costs are incurred at the same rate and at the same time during production. For example, raw materials might come in all at once at the beginning (or end) of the production process, while conversion costs (labor and overhead) are often incurred fairly evenly throughout production. Thus, for 100 physical units, we might have incurred 100% of the material costs (we have 100 "equivalent units of direct materials") but only incurred 20% of the conversion costs (we have 20 "equivalent units of conversion"). Once again, determining the number for our denominator (the total number of equivalent units made in the department in a given period) becomes more complicated: it depends on the cost type we are considering.

To address this complexity, we will compute a cost per equivalent unit by cost type, rather than in total. Note: this is only necessary if the costs are incurred at different times or different rates during production. For example, we can have a cost per equivalent unit for direct materials, a cost per equivalent unit for direct labor, and a cost per equivalent unit for overhead. Indeed, we could dissect our cost types even further. For example, if we had two types of direct material that enter production at different times during production, we could calculate a cost per equivalent unit for Direct Material 1 and a cost per equivalent unit for Direct Material 2. Often, because labor and overhead costs are incurred at about the same rate, we combine these two cost types into a single "conversion cost."

Using T-Accounts for Process Costing

There are multiple methods for calculating and tracking the flow of costs in process costing. Perhaps the most straightforward way is to organize physical units, equivalent units, and costs into multiple T-accounts.

EXAMPLE PROBLEM: JOW TOYS, INC. - MOLDING DEPARTMENT

Jow Toys, Inc. manufactures plastic yo-yos. The body of the yo-yo is produced in the molding department and is then transferred to the finishing department. In February, the molding department reported the following:

a. In the molding department, all direct materials are added at the beginning of the production process. Conversion costs are incurred evenly during production.

b. Beginning work in process consisted of 5,000 units, 20 percent complete with respect to direct labor and overhead. Costs in beginning inventory were for direct materials ($500) and conversion ($200).

c. Costs added to production during the month were for direct materials ($1,400) and conversion ($3,332).

d. During the month, 7,000 units were started. At the end of the month, the 4,000 units remaining in ending inventory were 70 percent complete.

e. For costing purposes, Jow assumes that the first units in are the first out (FIFO).

SOLUTION - PHYSICAL UNITS T-ACCOUNT:

Let's begin by considering the flow of physical units in the molding department. Since we know the beginning inventory of physical units (5,000), the new units we began work on (7,000), and the ending inventory (4,000), we can calculate the units transferred out (8,000).

Physical Units (Molding):
- Beginning: 5,000
- New Units: 7,000
- Transferred Out: 8,000 (calculated as plug)
- Ending: 4,000

SOLUTION - EQUIVALENT UNITS OF DIRECT MATERIAL:

Because the problem tells us that all materials are added as soon as production begins, we know that each physical unit is 100% complete with respect to direct materials. This means our T-account for equivalent units of direct materials will be identical to the physical units.

Equivalent Units of Direct Material (Molding):
- Beginning: 5,000
- New EU: 7,000
- Transferred Out: 8,000
- Ending: 4,000

SOLUTION - EQUIVALENT UNITS OF CONVERSION:

For conversion, we know that the beginning inventory is 20% complete with respect to direct labor and overhead (i.e., conversion), so we multiply the beginning inventory of physical units (5,000) by 20% to get the beginning inventory of equivalent units of conversion (1,000).

Next, we know that the ending inventory of physical units (4,000) is 70% complete with respect to conversion, so we multiply the ending inventory of physical units by 70% to get the ending inventory of equivalent units of conversion (2,800).

We also know that all units transferred out are 100% complete with respect to conversion, or we wouldn't be transferring them out. Thus, we multiply the units transferred out (8,000) by 100% to get the equivalent units of conversion transferred out (8,000).

Finally, because we know the beginning inventory, the ending inventory, and the units transferred out, we can calculate the new equivalent units of conversion this period (9,800).

Equivalent Units of Conversion (Molding):
- Beginning: 1,000 (5,000 × 20%)
- New EU: 9,800 (calculated as plug)
- Transferred Out: 8,000
- Ending: 2,800 (4,000 × 70%)

Note: The 9,800 equivalent units represent the work done during the current production period. If needed, we could directly compute this plug figure:
- Jow Toys had 5,000 units in beginning inventory. These units were 20% done, so Jow did another 80% of work on these units before they were transferred out: 5,000 × 0.80 = 4,000 equivalent units
- Then Jow started and completed another 3,000 units (8,000 units transferred out minus the 5,000 units that were originally in beginning inventory). Because all of the work for these 3,000 units that were started and completed was done this period, we have another 3,000 equivalent units.
- Finally, the ending inventory was 70% complete. Assuming FIFO, these units were started this period but not completed. In other words, all 70% of the work done on these units was done this period: 4,000 × 0.70 = 2,800 equivalent units
- All told: 4,000 + 3,000 + 2,800 = 9,800 equivalent units of work done in the current period.

SOLUTION - COST PER EQUIVALENT UNIT:

We now have all the information we need to calculate our cost per equivalent unit.

Direct Materials:
- New direct material costs this period: $1,400
- Equivalent units of direct material this period: 7,000
- Cost per equivalent unit of direct material: $1,400 ÷ 7,000 = $0.20

Conversion:
- New conversion costs this period: $3,332
- Equivalent units of conversion this period: 9,800
- Cost per equivalent unit of conversion: $3,332 ÷ 9,800 = $0.34

SOLUTION - DIRECT MATERIAL COST T-ACCOUNT:

We know that we incurred $1,400 in new direct material costs this period. We also know that we have $500 of direct materials costs in beginning inventory. Because Jow assumes FIFO, we know that we will transfer out at least $500 of direct materials costs (the costs associated with the 5,000 equivalent units of direct materials in beginning inventory).

But there are more costs to transfer out. We know that we transferred out 8,000 equivalent units of direct materials, and we want to know what cost is associated with these equivalent units. The $500 of direct materials costs in beginning inventory are the costs associated with the 5,000 equivalent units of direct materials in beginning inventory. To determine the cost of the remaining equivalent units of direct materials transferred we take 8,000 – 5,000 = 3,000 equivalent units to account for. We then multiply 3,000 by the cost per equivalent unit of direct materials: 3,000 × $0.20 = $600.

Direct Material Cost (Molding):
- Beginning: $500
- New Costs: $1,400
- Transferred Out (from Beg. Bal.): $500
- Transferred Out: $600
- Ending: $800 (calculated as plug)

IMPORTANT: We don't multiply the cost per equivalent unit by the total equivalent units transferred out (8,000). Doing so would imply that all 8,000 equivalent units of work was done this period; but we know that some of that work was done last period. When we transferred out the $500 that was in our beginning balance, we accounted for the cost associated with last period. By multiplying this period's cost per equivalent unit of direct materials by the difference between the units transferred out (8,000) and the units we started with in beginning inventory (5,000), we are calculating the new costs incurred this period to be transferred out.

SOLUTION - CONVERSION COST T-ACCOUNT:

We know that we have $3,332 in new conversion costs this period. We also know that we have $200 of conversion costs in beginning inventory. Assuming FIFO, we know that we will transfer out at least $200 of conversion costs—the costs associated with the 1,000 equivalent units of conversion in beginning inventory.

But we transferred out a total of 8,000 equivalent units of conversion, so we still have 8,000 – 1,000 = 7,000 equivalent units of conversion to account for. To determine the cost of these remaining equivalent units of conversion transferred out, we multiply 7,000 by the cost per equivalent unit of conversion: 7,000 × $0.34 = $2,380.

Conversion Cost (Molding):
- Beginning: $200
- New Costs: $3,332
- Transferred Out (from Beg. Bal.): $200
- Transferred Out: $2,380
- Ending: $952 (calculated as plug, or verified: 2,800 × $0.34 = $952)

SOLUTION - TOTAL COSTS:

Total cost transferred out of the molding department: $500 + $600 + $200 + $2,380 = $3,680

Total cost remaining in the molding department ending work in process: $800 + $952 = $1,752

---

PROCESS COSTING, PART 2

Multiple Production Departments

Most manufacturing processes involve several stages of production. For costing purposes, we divide these stages up into different departments. Usually, these departments match the physical flow of production, if not the layout of the factory floor. As units are transferred out of one department and go to another department, the costs go with them.

For example, in the problem given above, yo-yos are moved from the molding department to the finishing department. As the physical units are transferred out of the molding department and transferred in to the finishing department, the associated costs move with them. New costs will then be incurred in the second department.

However, it is important to recognize that while units are 100% complete with respect to costs from the previous department (by definition, or the units wouldn't have been transferred out of the previous department) the new costs incurred in the second department may be incurred over time. In other words, units may be only partially complete with respect to new costs in the current department, but will always be 100% complete with respect to costs transferred-in from the previous department.

Thus, in addition to potentially tracking direct materials costs, direct labor costs, and overhead costs separately in the new department, we must also track "transferred-in" costs separately. This will require the calculation of a "cost per equivalent unit transferred in," separate from our other costs per equivalent unit in the second (or later) department in the production process.

Spoilage

Spoilage in a production process refers to units, either fully- or partially-completed, that do not meet quality specifications and are discarded or sold at reduced prices.

Normal spoilage is spoilage that is considered inherent in the production process—it is a part of the cost of manufacturing good units. Thus, the cost of normal spoilage is included as part of the cost of non-spoiled units in inventory accounts on the balance sheet.

Abnormal spoilage should not happen under normal operating conditions and is considered avoidable. Because abnormal spoilage is not considered part of the cost of manufacturing good units (it is, as its name implies, abnormal), the costs associated with abnormal spoilage are not tracked in inventory accounts on the balance sheet (like other manufacturing costs), but are instead tracked on the income statement as a loss from abnormal spoilage.

Because work on a unit stops as soon as the unit is deemed to be spoiled, spoilage will further complicate our calculation of equivalent units: spoiled units may not have incurred as many costs as non-spoiled units if work on spoiled units was stopped before the unit was completed. If units are inspected when they are 100% complete, then the spoiled equivalent units equal the physical units deemed to be spoiled. If, however, inspection happens before units are 100% complete, spoiled equivalent units will be less than the physical units that are spoiled.

For example, if 100 units are inspected when they are 80% complete and 10 units are deemed spoiled, we only have 8 spoiled equivalent units.

Note: We typically assume that spoiled units were all new in the current period—they did not come from our beginning inventory. This will simplify our calculations and eliminate the need to attempt to distinguish between units that are identical.

EXAMPLE PROBLEM: JOW TOYS, INC. - FINISHING DEPARTMENT

Jow Toys, Inc. manufactures plastic yo-yos. The body of the yo-yo is transferred into the finishing department from the molding department. Conversion occurs continuously in the finishing department. Materials are added at the end of production in the finishing department (the string is attached and the yo-yo is moved to finished goods). In February, the finishing department reported the following:

a. Yo-yos are inspected in the finishing department when they are 80% complete with respect to conversion.

b. Beginning work in process consisted of 2,000 units, 40 percent complete with respect to conversion. Conversion costs in beginning inventory were $1,560. Transferred-in costs in beginning inventory were $1,264.

c. Costs added to production during the month for direct materials were $882 and for conversion were $2,226.

d. At the end of the month, the 2,500 units remaining in ending inventory were 30 percent complete.

e. For February, 7,350 units were transferred out to finished goods.

f. Normal spoilage for a given period is considered to be 100 units.

g. For costing purposes, Jow assumes that the first units in are the first out (FIFO).

SOLUTION - PHYSICAL UNITS T-ACCOUNT:

We know the beginning inventory of physical units (2,000), the ending inventory (2,500), and the units transferred out (7,350). From our earlier calculations, we also know that 8,000 units were transferred in from the molding department. Our plug number, then, is the number of units that were spoiled (150). Because this number is greater than 100, we have 100 physical units of normal spoilage and 50 units (150 – 100 = 50) of abnormal spoilage.

Physical Units (Finishing):
- Beginning: 2,000
- New Units: 8,000
- Transferred Out: 7,350
- Normal Spoilage: 100
- Abnormal Spoilage: 50
- Ending: 2,500

SOLUTION - EQUIVALENT UNITS TRANSFERRED-IN:

Because units are, by definition, 100% complete with respect to their transferred-in costs, our T-account for equivalent units transferred-in will be identical to the physical units. This includes our spoiled units, because these units have 100% of their transferred-in cost.

Equivalent Units Transferred-In (Finishing):
- Beginning: 2,000
- New EU: 8,000
- Transferred Out: 7,350
- Normal Spoilage: 100
- Abnormal Spoilage: 50
- Ending: 2,500

SOLUTION - EQUIVALENT UNITS OF CONVERSION:

For conversion, we know that the beginning inventory is 40% complete, so: 2,000 × 40% = 800 beginning equivalent units.

The ending inventory is 30% complete: 2,500 × 30% = 750 ending equivalent units.

All units transferred out are 100% complete: 7,350 × 100% = 7,350 equivalent units transferred out.

For spoilage, units are inspected when they are only 80% complete with respect to conversion:
- Normal spoilage: 100 × 80% = 80 equivalent units
- Abnormal spoilage: 50 × 80% = 40 equivalent units

New equivalent units of conversion this period: 7,420 (calculated as plug)

Equivalent Units of Conversion (Finishing):
- Beginning: 800
- New EU: 7,420
- Transferred Out: 7,350
- Normal Spoilage: 80
- Abnormal Spoilage: 40
- Ending: 750

SOLUTION - EQUIVALENT UNITS OF DIRECT MATERIAL:

Materials are not added until the end of production. This means physical units in beginning and ending inventory are 0% complete with respect to direct materials for the finishing department—if they had their materials (the string) they would be complete and would no longer be in work in process.

Units transferred out are 100% complete with respect to direct materials, so our plug number, the new equivalent units of direct materials, is equal to our units transferred out.

Note: Spoiled units have 0% of direct materials because they are inspected at 80% complete, before materials are added at 100%.

Equivalent Units of Direct Material (Finishing):
- Beginning: 0
- New EU: 7,350
- Transferred Out: 7,350
- Ending: 0

SOLUTION - COST PER EQUIVALENT UNIT:

Transferred-In:
- New transferred-in costs this period: $3,680
- Equivalent units transferred in: 8,000
- Cost per equivalent unit transferred in: $3,680 ÷ 8,000 = $0.46

Direct Materials:
- New direct material costs this period: $882
- Equivalent units of direct material this period: 7,350
- Cost per equivalent unit of direct material: $882 ÷ 7,350 = $0.12

Conversion:
- New conversion costs this period: $2,226
- Equivalent units of conversion this period: 7,420
- Cost per equivalent unit of conversion: $2,226 ÷ 7,420 = $0.30

SOLUTION - TRANSFERRED-IN COST T-ACCOUNT:

Transferred-In Cost (Finishing):
- Beginning: $1,264
- New Costs: $3,680
- Transferred Out (from Beg. Bal.): $1,264
- Transferred Out: $2,461 (calculated: (7,350 - 2,000) × $0.46 = 5,350 × $0.46)
- Normal Spoilage: $46 (100 × $0.46)
- Abnormal Spoilage: $23 (50 × $0.46)
- Ending: $1,150 (2,500 × $0.46)

SOLUTION - DIRECT MATERIAL COST T-ACCOUNT:

Direct Material Cost (Finishing):
- Beginning: $0
- New Costs: $882
- Transferred Out: $882 (7,350 × $0.12)
- Ending: $0

SOLUTION - CONVERSION COST T-ACCOUNT:

Conversion Cost (Finishing):
- Beginning: $1,560
- New Costs: $2,226
- Transferred Out (from Beg. Bal.): $1,560
- Transferred Out: $1,965 (calculated: (7,350 - 800) × $0.30 = 6,550 × $0.30)
- Normal Spoilage: $24 (80 × $0.30)
- Abnormal Spoilage: $12 (40 × $0.30)
- Ending: $225 (750 × $0.30)

SOLUTION - FINAL CALCULATIONS:

Total cost transferred to Finished Goods Inventory (includes normal spoilage):
$1,264 + $2,461 + $46 + $882 + $1,560 + $1,965 + $24 = $8,202

Total cost transferred to Loss from Abnormal Spoilage:
$23 + $0 + $12 = $35

Total cost remaining in ending work in process:
$1,150 + $0 + $225 = $1,375

SOLUTION - MASTER ACCOUNT (Work in Process Inventory - Finishing):

Work in Process Inventory (Finishing):
- Beginning: $2,824 ($1,264 + $1,560)
- New Costs: $6,788 ($3,680 + $882 + $2,226)
- Transferred Out (from Beg. Bal.): $2,824
- Transferred Out: $5,308
- Normal Spoilage: $70 ($46 + $24)
- Abnormal Spoilage: $35 ($23 + $12)
- Ending: $1,375

KEY FORMULAS FOR PROCESS COSTING:

1. Cost per Equivalent Unit = New Costs This Period / New Equivalent Units This Period

2. FIFO Equivalent Units = Units Transferred Out + Ending WIP EU - Beginning WIP EU

3. Weighted-Average Equivalent Units = Units Transferred Out + Ending WIP EU

4. Cost Transferred Out (FIFO) = Beginning Inventory Cost + (Units Transferred Out - Beginning Units) × Cost per EU

5. Ending Inventory Cost = Ending Equivalent Units × Cost per Equivalent Unit

6. Total Cost Transferred to Finished Goods = All Transferred Out Costs + Normal Spoilage Costs

7. Loss from Abnormal Spoilage = Abnormal Spoilage Units × Cost per EU (for each cost type)

===
END OF TEXTBOOK CONTENT
"""


FULL_TAX_TEXTBOOK_CONTENT = """
================================================================================
=== COMPLETE TEXTBOOK CONTENT FOR ACC 405 - FEDERAL TAX ACCOUNTING ===
================================================================================

This is the authoritative source for all ACC 405 Tax Accounting questions.
When answering questions, always cite the specific chapter and section.

================================================================================
TUTOR INSTRUCTIONS AND GUIDELINES
================================================================================

1. Core Responsibilities

Primary Source: Use the provided textbook content as the "Gold Standard" for all explanations. If a specific tax rule or threshold in the textbook differs from general knowledge (due to the tax year the book covers), prioritize the textbook's version.

Code Citations: Whenever possible, link concepts to the relevant Internal Revenue Code (IRC) Sections or Treasury Regulations if mentioned in the text.

Logical Framework: Teach tax through the "Tax Formula" (Gross Income → Adjustments → AGI → Deductions → Taxable Income). Always clarify if a deduction is Above-the-Line (for AGI) or Itemized (from AGI).

Practice Problems: Generate "Fact Patterns" where the user must calculate a taxpayer's tax liability, basis in property, or deductible amount based on the provided text.

2. Formatting & Style Guidelines

Tax Tables: Use Markdown tables to display tax brackets, standard deductions, and phase-out thresholds for clarity.

Calculations: Use LaTeX for all mathematical steps.

Visual Organization: Use bolding for critical terms (e.g., Constructive Receipt, Capital Asset, Material Participation).

3. Interaction Protocols

The "Socratic" Method: If the user asks for an answer to a homework problem, do not give it immediately. Ask clarifying questions to guide them to the answer.

Update Alerts: If a user asks about a law that has significantly changed in 2026, acknowledge the textbook's rule first, then provide a brief "Real-World 2026 Update" for context.

Exam Readiness: At the end of a session, offer to create a "Quick Reference Sheet" for the chapter discussed.

================================================================================
CHAPTER 4: THE INDIVIDUAL INCOME TAX FORMULA
================================================================================

LO 4-1: The Individual Income Tax Formula

Taxable income is the tax base for the individual income tax. The formula includes four new from AGI deductions introduced by the One Beautiful Big Bill Act of 2025 (OBBBA), signed into law on July 4, 2025.

EXHIBIT 4-1: Individual Income Tax Formula

Gross income
Minus: For AGI (above the line) deductions
Equals: Adjusted gross income (AGI)
Minus: From AGI (below the line) deductions:
    (1) Greater of:
        (a) Standard deduction or
        (b) Itemized deductions
    (2) Deductions for seniors*
    (3) Deduction for qualified car loan interest*
    (4) Deduction for qualified tip income*
    (5) Deduction for qualified overtime compensation*
    (6) Deduction for qualified business income
Equals: Taxable income
Times: Tax rates
Equals: Income tax liability
Plus: Other taxes
Equals: Total tax
Minus: Credits
Minus: Prepayments
Equals: Taxes due or (refund)

*Deductions introduced by the One Big Beautiful Bill Act of 2025.

---

GROSS INCOME

The U.S. tax laws are based on the all-inclusive income concept. Under this concept, gross income generally includes all realized income from whatever source derived. Realized income is generally income generated in a transaction with a second party in which there is a measurable change in property rights between parties.

Certain tax provisions allow taxpayers to permanently exclude specific types of realized income from gross income (exclusions), and other provisions allow taxpayers to defer including certain types of realized income items in gross income until a subsequent year (deferrals).

EXHIBIT 4-3: Partial Listing of Common Income Items

| Income Item | Character |
|-------------|-----------|
| Compensation for services including fringe benefits | Ordinary |
| Business income | Ordinary |
| Gains from selling property | Ordinary or capital |
| Interest and dividends | Ordinary or qualified dividend |
| Rents and royalties | Ordinary |
| Alimony received (pre-2019 decree) and annuities | Ordinary |
| Retirement income | Ordinary |
| Income from the discharge of indebtedness | Ordinary |

EXHIBIT 4-4: Partial Listing of Common Exclusions and Deferrals

| Item | Exclusion or Deferral |
|------|----------------------|
| Interest income from municipal bonds | Exclusion |
| Gifts and inheritance | Exclusion |
| Alimony received (post-2018 decree) | Exclusion |
| Gain on sale of personal residence | Exclusion |
| Life insurance proceeds | Exclusion |
| Installment sale | Deferral |
| Like-kind exchange | Deferral |

---

CHARACTER OF INCOME

The type of income is commonly referred to as the character of income. The most common characters are:

**Ordinary:** Income or loss taxed at ordinary rates provided in the tax rate schedules, and is not capital in character.

**Capital:** Gains or losses on the disposition or sale of capital assets. Capital assets are all assets other than:
- Accounts receivable from the sale of goods or services
- Inventory and other assets held for sale in the ordinary course of business
- Assets used in a trade or business, including supplies

Thus, capital assets include nonbusiness assets such as personal-use automobiles or personal residences and assets held for investment such as stocks and bonds.

The capital gain or loss from the sale of a particular capital asset is:
- Long-term: when the taxpayer has owned the asset for MORE than a year before selling
- Short-term: when the taxpayer has owned the asset for one year or LESS before selling

When determining holding period, the acquisition date is NOT counted but the disposition date IS counted.

Capital Gain/Loss Netting Process:
1. Sort capital gains/losses into long-term and short-term categories
2. Combine gains and losses within each category
3. If both categories yield gains or both yield losses, netting is complete
4. Otherwise, combine long-term and short-term outcomes for a final net gain or loss

Taxpayers may deduct up to $3,000 of net capital loss for the year ($1,500 for married filing separately). Net capital losses are deducted for AGI. Excess losses carry over to the next year.

Net short-term capital gains are taxed at ordinary income rates. Net long-term capital gains (net capital gains) are taxed at preferential rates of 0%, 15%, or 20% depending on taxable income level.

**Qualified dividend:** Dividends meeting the qualified dividend requirements are taxed at the same preferential rate as net capital gains. Non-qualified dividends are taxed at ordinary rates. Qualified dividends are NOT included in the capital gain/loss netting process.

Example 4-1:
Rodney earned a salary of $84,000, and Anita earned a salary of $66,000. They also received $600 of interest income from corporate bonds and $300 of interest income from municipal bonds.

Gross income = $150,600 ($84,000 + $66,000 + $600)
*The $300 of municipal bond interest is excluded from gross income.

Character: Salary and corporate bond interest are ordinary income. Municipal bond interest is excluded.

---

DEDUCTIONS

Deductions reduce taxable income. Unlike the all-inclusive treatment of income, deductions are not allowed unless a specific tax law allows them. Thus, deductions are a matter of legislative grace.

Two types of deductions:
1. For AGI deductions (above the line)
2. From AGI deductions (below the line)

Gross income - For AGI deductions = AGI
AGI - From AGI deductions = Taxable income

KEY FACTS: For and From AGI Deductions

For AGI deductions:
- Reduce AGI
- Referred to as deductions "above the line"
- Generally more valuable than from AGI deductions

From AGI deductions:
- Deduct from AGI to determine taxable income
- Referred to as deductions "below the line"

---

FOR AGI DEDUCTIONS

For AGI deductions tend to be associated with business activities and certain investing activities. The "line" is AGI (line 11 on Form 1040).

EXHIBIT 4-5: Partial Listing of Common for AGI Deductions

| For AGI Deduction |
|-------------------|
| Alimony paid (pre-2019 decree) |
| Health insurance deduction for self-employed taxpayers |
| Rental and royalty expenses |
| Net capital losses [limited to $3,000 ($1,500 for MFS)] |
| One-half of self-employment taxes paid |
| Business expenses |
| Losses on dispositions of assets used in a trade or business |
| Contributions to qualified retirement accounts (401k, traditional IRA) |

---

FROM AGI DEDUCTIONS

From AGI deductions include:
- Itemized deductions OR standard deduction (greater of the two)
- Qualified business income (QBI) deduction
- Four OBBBA deductions (seniors, car loan interest, tip income, overtime compensation)

The QBI deduction and the four OBBBA deductions are deductible regardless of whether a taxpayer itemizes or takes the standard deduction.

EXHIBIT 4-6: Primary Categories of Itemized Deductions

Medical and dental expenses: Deductible to the extent exceeding 7.5% of AGI.

Taxes: State and local income taxes, sales taxes, real estate taxes, personal property taxes [OBBBA limits aggregate deduction to $40,000 ($20,000 if MFS)].

Interest expense: Mortgage and investment interest expense.

Gifts to charity (charitable contributions).

Other miscellaneous deductions: Gambling losses (to extent of winnings) and certain other deductions.

EXHIBIT 4-7: Standard Deduction Amounts by Filing Status

| Filing Status | 2024 | 2025 |
|---------------|------|------|
| Married filing jointly | $29,200 | $31,500 |
| Qualifying surviving spouse | $29,200 | $31,500 |
| Married filing separately | $14,600 | $15,750 |
| Head of household | $21,900 | $23,625 |
| Single | $14,600 | $15,750 |

Additional standard deduction for age 65+ and/or blind:
- 2025: $1,600 for married taxpayers; $2,000 for unmarried taxpayers
- 2024: $1,550 for married taxpayers; $1,950 for unmarried taxpayers

For dependents: Standard deduction is greater of (1) $1,350 or (2) $450 plus earned income, not to exceed the regular standard deduction.

EXHIBIT 4-8: From AGI Deductions (OBBBA Provisions)

**Deduction for seniors:** $6,000 for taxpayers at least age 65 at year-end. Subject to AGI-based phase-out. Not available for MFS.

**Deduction for qualified car loan interest:** Up to $10,000. Loan must be for vehicle purchased after December 31, 2024, with final assembly in the United States. Subject to AGI-based phase-out.

**Deduction for qualified tip income:** Up to $25,000 of qualified tips received. Subject to AGI-based phase-out. Not available for MFS.

**Deduction for qualified overtime compensation:** Up to $12,500 ($25,000 if MFJ) of qualified overtime compensation. Subject to AGI-based phase-out. Not available for MFS.

**Deduction for qualified business income:** 20% of QBI, subject to phase-out based on taxable income before the QBI deduction.

---

INCOME TAX CALCULATION

After determining taxable income, taxpayers calculate regular income tax liability using tax tables (if taxable income under $100,000) or tax rate schedules.

---

OTHER TAXES

In addition to regular income tax, individuals may pay:
- Alternative minimum tax (AMT)
- Self-employment taxes
- 3.8% net investment income tax (on unearned income for high-AGI taxpayers)
- 0.9% additional Medicare tax (on earned income for high-AGI taxpayers)

---

TAX CREDITS

Tax credits directly reduce taxes payable (unlike deductions, which reduce taxable income).

A $1 deduction reduces taxes by $1 × marginal tax rate
A $1 credit reduces taxes by $1

Common tax credits:
- Child tax credit: $2,200 for qualifying children under age 17
- $500 credit for other qualifying dependents
- Child and dependent care credit
- Earned income credit
- American opportunity credit
- Lifetime learning credit

These credits are subject to full or partial phase-out for higher-income taxpayers.

---

TAX PREPAYMENTS

Tax prepayments include:
1. Withholdings from salary, wages, or other income sources
2. Estimated tax payments made directly to IRS
3. Prior-year overpayments applied to current year

If prepayments > total tax after credits → refund
If prepayments < total tax after credits → tax due (and potentially underpayment penalty)

================================================================================
LO 4-2: DEPENDENTS OF THE TAXPAYER
================================================================================

Although taxpayers cannot claim a deduction for dependents, determining who qualifies as a dependent is necessary for:
- Filing status determination
- Eligibility for certain tax credits
- Other tax-related computations

DEPENDENCY REQUIREMENTS

To qualify as a dependent, an individual must:
1. Be a citizen or resident of the United States, Canada, or Mexico
2. Not file a joint return with their spouse (with limited exceptions)
3. Be either a qualifying child OR a qualifying relative of the taxpayer

---

QUALIFYING CHILD

Must satisfy four tests: (1) relationship, (2) age, (3) residence, and (4) support.

**Relationship test:**
Must be an eligible relative including:
- Child or descendant of a child (includes adopted child, stepchild, eligible foster child)
- Sibling or descendant of sibling (includes half-brother, half-sister, stepbrother, stepsister)

**Age test:**
Must be younger than the taxpayer AND either:
- Under age 19 at end of year, OR
- Under age 24 at end of year and a full-time student (in school full-time during any part of 5 calendar months)
- Exception: Any age if permanently and totally disabled

**Residence test:**
Must have same principal residence as taxpayer for more than half the year. Temporary absences (illness, education, etc.) count as living in taxpayer's home.

**Support test:**
The qualifying child must NOT have provided more than half of their own support. Support includes: food, clothing, recreation, medical care, child care, lodging, education (scholarships excluded from calculation for full-time students).

TIEBREAKING RULES (when person is qualifying child to multiple taxpayers):

1. Parent vs. nonparent: Parent has priority
2. Multiple parents: Parent with whom child resided longest has priority; if equal time, parent with higher AGI
3. Multiple nonparents: Nonparent with highest AGI has priority

Note: Noncustodial parent can claim child if custodial parent signs Form 8332.

---

QUALIFYING RELATIVE

A person who is NOT a qualifying child and satisfies: (1) relationship test, (2) support test, and (3) gross income test.

**Relationship test (more inclusive than qualifying child):**
Either:
- Has a "qualifying family relationship" with taxpayer (descendant, ancestor, sibling, stepparent, niece/nephew, aunt/uncle, in-laws), OR
- Lives with taxpayer for entire year as member of household

Note: Cousins do NOT qualify under the family relationship test.

**Support test:**
Taxpayer must pay MORE than half of the qualifying relative's support/living expenses.

Multiple Support Agreement: When no one taxpayer pays over half:
- Taxpayer and others together provide over half the support
- Taxpayer contributed over 10% of support
- Others who contributed over 10% sign statements agreeing not to claim the dependent

**Gross income test:**
Qualifying relative's gross income must be less than $5,200 in 2025.

EXHIBIT 4-9: Summary of Dependency Requirements

| Test | Qualifying Child | Qualifying Relative |
|------|------------------|---------------------|
| Relationship | Child, stepchild, foster child, sibling, or descendant | Descendant, ancestor, sibling, step-relatives, in-laws, OR member of household for entire year |
| Age | Under 19, or under 24 if full-time student, or any age if disabled. Must be younger than taxpayer. | Not applicable |
| Residence | Lives with taxpayer more than half the year | Not applicable |
| Support | Child must NOT provide more than half of own support | Taxpayer must provide MORE than half of support |
| Gross income | Not applicable | Less than $5,200 (2025) |
| Other | Not applicable | Not a qualifying child |

An individual who is a dependent of another CANNOT claim any dependents.

================================================================================
LO 4-3: FILING STATUS
================================================================================

Filing status is determined by marital status at year-end and whether the taxpayer has dependents.

Filing status determines:
- Applicable tax rate schedule
- Standard deduction amount
- AGI thresholds for tax benefit reductions

Five filing statuses:
1. Married filing jointly (MFJ)
2. Married filing separately (MFS)
3. Qualifying surviving spouse (QSS)
4. Single
5. Head of household (HoH)

---

MARRIED FILING JOINTLY AND MARRIED FILING SEPARATELY

To be married for tax purposes, must be married on the LAST DAY of the year. If spouse dies during year, surviving spouse is considered married at year-end (unless remarried).

**MFJ:** Combine income and deductions; share joint and several liability (both responsible for entire tax).

**MFS:** Each spouse reports own income and deductions separately. Tax items are generally half of MFJ amounts. If one spouse itemizes, the other must also itemize (even if standard deduction is higher).

Generally, MFS is a tax disadvantage but may be chosen for non-tax reasons (liability protection, not in contact with spouse).

---

ABANDONED SPOUSE (Married Individual Treated as Unmarried)

A married taxpayer is treated as unmarried if ALL of the following are met:
1. Married at end of year (or not legally separated)
2. Does not file joint return
3. Pays more than half the costs of maintaining home for entire year
4. Home is principal residence for a child (who is taxpayer's dependent) for more than half the year
5. Lived apart from other spouse for last six months of year

Taxpayers meeting these requirements qualify for head of household filing status.

---

QUALIFYING SURVIVING SPOUSE

Available for TWO years after year of spouse's death if:
1. Taxpayer remains unmarried
2. Taxpayer pays over half the cost of maintaining household where a dependent child lived for the entire year

The dependent child must be a child or stepchild (not foster child) of the taxpayer.

---

SINGLE

Unmarried taxpayers who do not qualify for head of household.

---

HEAD OF HOUSEHOLD

More favorable than MFS and Single, but less favorable than MFJ and QSS.

Requirements:
1. Unmarried (or treated as unmarried under abandoned spouse rules) at year-end
2. Not a qualifying surviving spouse
3. Pay more than half the costs of keeping up a home for the year
4. Have a "qualifying person" live in taxpayer's home for more than half the year

Exception: If qualifying person is taxpayer's dependent PARENT, the parent does NOT have to live with the taxpayer (but taxpayer must pay over half the cost of parent's household).

Special rules:
- A qualifying person may only qualify ONE taxpayer for HoH status
- Multiple support agreement dependents are NOT qualifying persons
- For divorced parents, custodial parent can use child as qualifying person even if noncustodial parent claims the dependency exemption

KEY FACTS: Filing Status Summary

**Married taxpayers:**
- MFJ: Both spouses liable for joint tax
- MFS: Each spouse liable only for own tax; generally a disadvantage
- QSS: Available 2 years after spouse's death if maintaining household for dependent child

**Unmarried taxpayers:**
- Single: No dependents (or no qualifying person)
- HoH: Maintaining household for qualifying person

================================================================================
CHAPTER 5: REALIZATION AND RECOGNITION OF INCOME
================================================================================

LO 5-1: What Is Included in Gross Income?

IRC §61(a): "Gross income means all income from whatever source derived."

Reg. §1.61-1(a): "Gross income means all income from whatever source derived, unless excluded by law. Gross income includes income realized in any form, whether in money, property, or services."

Taxpayers recognize gross income when:
1. They receive an economic benefit
2. They realize the income
3. No tax provision allows them to exclude or defer the income

---

ECONOMIC BENEFIT

Must receive something of value (cash, property, services, or debt relief).

Borrowing money is NOT an economic benefit because the cash received is offset by the liability to repay.

---

REALIZATION PRINCIPLE

Income is realized when:
1. A transaction occurs with another party
2. The transaction results in a measurable change in property rights

Advantages of realization principle:
1. Objective measurement (parties agree to value)
2. Wherewithal to pay (transaction provides funds for taxes)

---

RECOGNITION

Taxpayers must include realized economic benefits in gross income unless a specific provision allows exclusion or deferral.

---

OTHER INCOME CONCEPTS

**Form of Receipt:**
Income is realized whether received as money, property, or services. Barter transactions create taxable income at fair market value.

**Return of Capital Principle:**
When selling property, taxpayers may recover their cost (tax basis) tax-free. Only the gain (proceeds minus basis) is taxable.

**Tax Benefit Rule:**
Refunds of previously deducted amounts are included in income to the extent the prior deduction produced a tax benefit.

---

WHEN DO TAXPAYERS RECOGNIZE INCOME?

KEY FACTS: Income Recognition
- Cash-method taxpayers recognize income when received
- Income is realized regardless of form (money, property, or services)
- Income is taxed when taxpayer has right to receive without substantial restrictions

**Accounting Methods:**
- Accrual method: Income recognized when earned; expenses deducted when incurred
- Cash method: Income recognized when received; expenses deducted when paid
Most individuals use the cash method.

**Constructive Receipt Doctrine:**
Cash-method taxpayers recognize income when actually or constructively received. Constructive receipt occurs when:
- Income is credited to taxpayer's account, OR
- Income is unconditionally available to taxpayer
- Taxpayer is aware of availability
- No restrictions on taxpayer's control

Example: Bonus check available December 28 but not picked up until January 2 is taxable in the year it became available.

**Claim of Right Doctrine:**
Income is realized if received with no restrictions on use (no obligation to repay).

---

WHO RECOGNIZES THE INCOME?

**Assignment of Income Doctrine:**
- Income from services is taxed to the person who EARNED it
- Income from property is taxed to the person who OWNS the property

To shift income from property, must transfer ownership of the property itself.

**Community Property Systems:**
Nine states: Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, Wisconsin

In community property states:
- Half of each spouse's earned income is included in the other spouse's gross income
- Half of community property income is included in each spouse's gross income

================================================================================
LO 5-2: TYPES OF INCOME
================================================================================

**INCOME FROM SERVICES (Earned Income)**

Includes salary, wages, fees, and unemployment compensation. Rarely exempt from taxation.

---

**INCOME FROM PROPERTY (Unearned Income)**

Includes gains/losses from property sales, dividends, interest, rents, royalties, and annuities.

Qualified dividends and long-term capital gains are taxed at preferential rates.

---

**ANNUITIES**

An investment paying a stream of equal payments over time.

Two types:
1. Fixed period annuities
2. Life annuities

Tax treatment: Part of each payment is nontaxable return of capital; remainder is gross income.

Annuity Exclusion Ratio = Original Investment / Expected Value of Annuity

For fixed annuities: Expected value = number of payments × payment amount

For life annuities: Use IRS tables for expected return multiple based on age.

EXHIBIT 5-1: Expected Return Multiple for Single-Life Annuity

| Age at Start | Expected Return Multiple |
|--------------|-------------------------|
| 68 | 17.6 |
| 69 | 16.8 |
| 70 | 16.0 |
| 71 | 15.3 |
| 72 | 14.6 |

If taxpayer outlives life expectancy: "Extra" payments are fully taxable.
If taxpayer dies early: Unrecovered investment is deducted on final return.

---

**PROPERTY DISPOSITIONS**

EXHIBIT 5-2: Formula for Gain/Loss

Sales proceeds
- Selling expenses
= Amount realized
- Tax basis (investment)
= Gain (Loss) on sale

KEY FACTS: Return of Capital
- Taxpayers recover capital invested tax-free
- Annuity payments are part income, part return of capital
- Gain/loss = sale proceeds minus tax basis

---

**OTHER SOURCES OF GROSS INCOME**

**Income from Flow-Through Entities:**
Partnership and S corporation income "flows through" to owners based on ownership percentage. Owners are taxed on their share whether or not cash is distributed. Each item retains its character (e.g., dividends remain dividends).

**Alimony:**
Definition: Cash transfer under written separation agreement or divorce decree; not designated as other than alimony; spouses don't live together; payments stop at recipient's death.

Pre-2019 agreements: Alimony is income to recipient, deductible for AGI by payor.
Post-2018 agreements: Alimony is NOT income to recipient, NOT deductible by payor.

Child support: Never taxable to recipient, never deductible by payor.
Property divisions: Not taxable events.

**Prizes, Awards, and Gambling Winnings:**
Generally included in gross income.

Exceptions:
1. Scientific/literary/charitable awards (Nobel Prize) if: selected without entering; no future services required; transferred to charity
2. Employee awards for length of service/safety: up to $400 of tangible property
3. Olympic medals/prize money if AGI doesn't exceed $1 million

Gambling: Include all winnings in gross income; deduct losses only to extent of winnings (as itemized deduction).

**Social Security Benefits:**
Up to 85% may be taxable depending on filing status and modified AGI.

Single taxpayers:
- Modified AGI + 50% of benefits ≤ $25,000: Not taxable
- $25,000 < Modified AGI + 50% of benefits ≤ $34,000: Lesser of 50% of benefits or 50% of (Modified AGI + 50% of benefits - $25,000)
- Modified AGI + 50% of benefits > $34,000: Up to 85% taxable

MFJ taxpayers:
- Thresholds are $32,000 and $44,000

MFS taxpayers:
- Up to 85% of benefits taxable (no favorable threshold)

**Imputed Income:**
Indirect economic benefits included in gross income.

Bargain purchases:
- Employee from employer: Taxable compensation (but discounts on goods up to employer's gross profit % and services up to 20% are excluded)
- Shareholder from corporation: Taxable dividend
- Family members: Gift

Below-market loans:
- Imputed interest = Loan principal × (Federal rate - Actual rate)
- Imputed interest is income to lender, expense to borrower
- The "return" of imputed interest is treated based on relationship (compensation, dividend, or gift)
- Exception: Loans of $10,000 or less

**Discharge of Indebtedness:**
Generally included in gross income when debt is forgiven.

Exceptions:
- Insolvent taxpayers: Excluded to extent of insolvency
- Student loan discharges: Most excluded after 2020 and before 2026

KEY FACTS: Other Sources of Income
- Pre-2019 alimony: Taxable to recipient
- Post-2018 alimony: Not taxable to recipient
- Awards: Generally taxable unless meeting narrow exceptions
- Social Security: Up to 85% taxable depending on AGI
- Discharge of debt: Taxable unless insolvent

================================================================================
LO 5-3: EXCLUSION PROVISIONS
================================================================================

Exclusions allow taxpayers to permanently remove certain income from the tax base.

Congress allows exclusions for two primary reasons:
1. To subsidize or encourage particular activities
2. To be fair to taxpayers (mitigate double taxation)

---

**COMMON EXCLUSIONS**

**Municipal Bond Interest:**
Interest on state and local government bonds is excluded from federal gross income. This subsidizes state/local governments by allowing them to offer lower interest rates.

Note: U.S. government bond interest (Treasury bills) IS taxable for federal purposes but exempt for state/local purposes.

**Gains on Sale of Personal Residence:**
Exclude up to $250,000 ($500,000 if MFJ) of gain.

Requirements:
- Ownership test: Owned residence for 2+ years during 5-year period ending on sale date
- Use test: Used as principal residence for 2+ years during 5-year period ending on sale date

Limited to one exclusion every two years.

MFJ: Full $500,000 if either spouse meets ownership test and BOTH meet use test. Reduced to $250,000 if either spouse used exclusion in prior 2 years.

**Fringe Benefits:**
Many employer-provided benefits are excluded from employee's gross income.

EXHIBIT 5-3: Common Qualified Fringe Benefits

| Benefit | Exclusion |
|---------|-----------|
| Medical/dental insurance [§106] | Full exclusion |
| Group-term life insurance [§79] | Up to $50,000 coverage |
| De minimis benefits [§132(a)(4)] | Small, infrequent benefits |
| Meals and lodging [§119] | If on premises, for employer's convenience, and lodging is condition of employment |
| Educational assistance [§127] | Up to $5,250 |
| No additional cost services [§132(a)(1)] | Services with no substantial cost to employer |
| Qualified employee discounts [§132(a)(2)] | Goods up to gross profit %; services up to 20% |
| Dependent care benefits [§129] | Up to $5,000 |
| Working condition fringe [§132(a)(3)] | Benefits that would be deductible if employee paid |
| Qualified transportation [§132(a)(5)] | Up to $325/month parking; up to $325/month transit |
| Cafeteria plans [§125] | Tax-free to extent choosing nontaxable benefits |
| FSA (medical) [§125] | Up to $3,300 in 2025; $660 carryover |
| HSA [§106; §223] | Up to $4,300 self-only ($8,550 family) in 2025; extra $1,000 if age 55+ |

Employee expense reimbursements: Excluded under an accountable plan (requires documentation of legitimate business expenses).

---

**EDUCATION-RELATED EXCLUSIONS**

**Scholarships:**
Excludable: Tuition, fees, books, supplies, required equipment (for degree-seeking students).
Taxable: Room, board, payments for services.

Athletic scholarships: Excludable if university expects but doesn't require participation; not cancelled if student can't participate. NIL payments are fully taxable.

KEY FACTS: Education Exclusions
- Scholarships for tuition/fees/books/supplies are excludable
- Room and board are taxable
- Series EE bond interest is excludable if used for qualified higher education (subject to AGI phase-out)

**529 Plans:**
Earnings distributed tax-free if used for:
- Qualified higher-education expenses (no annual limit)
- K-12 tuition ($10,000 limit in 2025; $20,000 in 2026)

**Coverdell Accounts:**
$2,000 annual contribution limit per beneficiary. Earnings tax-free for qualified education expenses (K-12 and higher education). Contribution eligibility phases out at AGI $190,000-$220,000 (MFJ) or $95,000-$110,000 (others).

**U.S. Series EE Bonds:**
Interest excludable if proceeds used for higher-education expenses of taxpayer, spouse, or dependent. Subject to modified AGI phase-out.

---

**EXCLUSIONS THAT MITIGATE DOUBLE TAXATION**

**Gifts and Inheritances:**
Excluded from recipient's income. Subject to transfer taxes (gift tax or estate tax) paid by transferor.

**Life Insurance Proceeds:**
Death benefits excluded from beneficiary's income.
Exceptions:
- Installment payments: Interest portion is taxable
- Policy transferred for valuable consideration: Only purchase price and subsequent premiums excluded

Early receipt:
- Terminally ill (expected death within 24 months): Fully excluded
- Chronically ill: Excluded to extent used for long-term care

Cashing out policy: Recognize ordinary income to extent proceeds exceed premiums paid.

**Foreign-Earned Income:**
Exclude up to $130,000 (2025) of foreign-earned income from personal services.

Requirements: Tax home in foreign country AND either:
- Bona fide resident of foreign country for entire calendar year, OR
- Present in foreign country for 330 days in consecutive 12-month period

Pro-rated if qualifying period spans two tax years.

Housing exclusion: Employer-provided housing costs exceeding 16% of $130,000 ($20,800), up to 14% of $130,000 ($18,200).

KEY FACTS: Exclusions to Mitigate Double Taxation
- Gifts and inheritances: Excluded (subject to transfer taxes)
- Foreign-earned income: Up to $130,000 (2025) if meeting residency requirements
- Life insurance: Death benefits excluded

---

**SICKNESS AND INJURY-RELATED EXCLUSIONS**

KEY FACTS: Sickness and Injury Exclusions
- Workers' compensation: Fully excluded
- Physical injury damages: Excluded (but punitive damages are taxable)
- Health insurance reimbursements: Excluded
- Disability benefits: Excluded if taxpayer paid premiums (or employer-paid premiums were taxable compensation)

**Workers' Compensation:**
Payments from state-sponsored workers' compensation plans are excluded. (Unemployment compensation is fully TAXABLE.)

**Payments for Personal Injury:**
Compensatory damages for physical injury or physical sickness: Excluded (including emotional distress associated with physical injury).
Punitive damages: Fully taxable.
Emotional distress NOT associated with physical injury: Taxable.

**Health Care Reimbursement:**
Reimbursements from health and accident insurance for medical expenses are excluded (regardless of who purchased the policy).

**Disability Insurance:**
Disability benefits are excluded if:
- Taxpayer purchased the policy, OR
- Employer-paid premiums were treated as taxable compensation to employee

If employer-paid premiums were a nontaxable fringe benefit: Disability benefits are TAXABLE.

================================================================================
CHAPTER 6: INDIVIDUAL DEDUCTIONS
================================================================================

LO 6-1: DEDUCTIONS FOR AGI

Congress allows taxpayers to claim a variety of deductions for AGI, classified into three categories:
1. Deductions directly related to business activities
2. Deductions indirectly related to business activities
3. Deductions subsidizing specific activities

---

DEDUCTIONS DIRECTLY RELATED TO BUSINESS ACTIVITIES

Business activities (trade or business): Require a relatively high level of involvement or effort. Examples: full-time employee, self-employed individuals.

Investment activities: Profit-motivated but don't require high degree of involvement. Examples: buying land or stock for appreciation.

EXHIBIT 6-1: Business and Investment Expense Deductions

| Activity Type | For AGI | From AGI | Not Deductible |
|---------------|---------|----------|----------------|
| Business | Self-employed business expenses | QBI deduction; Tip income deduction; Overtime deduction | Unreimbursed employee expenses |
| Investment | Rental and royalty expenses | Investment interest expense | Other investment expenses |

**Trade or Business Expenses:**
Deductible if directly related to business and ordinary and necessary for the activity. Reported on Schedule C.

**Rental and Royalty Expenses:**
Deductible for AGI on Schedule E, even if activity is considered an investment rather than a trade or business.

**Losses on Dispositions:**
Business asset losses: Deductible for AGI.
Capital losses: Deductible against capital gains; up to $3,000 net capital loss per year ($1,500 for MFS). Excess carries forward indefinitely.

**Flow-Through Entities:**
Partnership, LLC, and S corporation income/losses flow through to owners on Schedule E, subject to basis, at-risk, passive loss, and excess business loss limitations.

**Excess Business Loss Limitation:**
Taxpayers cannot deduct excess business losses. Excess = aggregate business deductions minus (aggregate business income + threshold amount).

Threshold amounts for 2025:
- MFJ: $626,000
- All others: $313,000

Excess business losses carry forward as NOL.

---

DEDUCTIONS INDIRECTLY RELATED TO BUSINESS ACTIVITIES

**Moving Expenses:**
Generally NOT deductible (and employer reimbursements are taxable).
Exception: Members of Armed Forces on active duty moving pursuant to military order.

**Health Insurance Deduction for Self-Employed:**
Self-employed taxpayers may deduct health insurance premiums for self, spouse, dependents, and children under 27 as a for AGI deduction.
Limited to self-employment income from the specific trade or business.
NOT allowed if eligible to participate in employer-provided health plan (including spouse's employer plan).

**Self-Employment Tax Deduction:**
Self-employed individuals pay self-employment tax (both employee and employer shares of Social Security and Medicare).
May deduct the EMPLOYER PORTION (50%) of self-employment tax for AGI.

**Deductions for IRAs:**
Deductible contributions to traditional IRAs are for AGI deductions.
Amount depends on filing status, participation in employer-sponsored plan, and modified AGI.
Distributions taxed as ordinary income; early distributions (before 59½) subject to 10% penalty.

**Health Savings Accounts (HSAs):**
For individuals covered by high-deductible health plan with no other health coverage.

2025 high-deductible plan requirements:
- Minimum deductible: $1,650 self-only; $3,300 family
- Maximum out-of-pocket: $8,300 self-only; $16,600 family

2025 contribution limits (deductible for AGI):
- $4,300 self-only; $8,550 family
- Additional $1,000 if age 55+

Distributions tax-free if for qualified medical expenses. Otherwise taxed as ordinary income plus 20% penalty (unless disabled, 65+, or deceased).

**Penalty for Early Withdrawal of Savings:**
Interest forfeited as penalty for early CD withdrawal is deductible for AGI.

---

DEDUCTIONS SUBSIDIZING SPECIFIC ACTIVITIES

**Interest on Qualified Education Loans:**

KEY FACTS: Education Loan Interest
- Up to $2,500 deductible for AGI
- Must be qualified education loan (proceeds for qualified education expenses)
- Phase-out for higher AGI taxpayers

Qualified education expenses: Tuition, fees, books, room and board, other necessary expenses for taxpayer, spouse, or dependent attending postsecondary institution.

EXHIBIT 6-4: Education Loan Interest Limitations

| Modified AGI | Deduction |
|--------------|-----------|
| Not over $85,000 ($170,000 MFJ) | Up to $2,500 |
| $85,000-$100,000 ($170,000-$200,000 MFJ) | Phased out |
| $100,000+ ($200,000+ MFJ) | Zero |

Phase-out percentage:
- Single/HoH: (Modified AGI - $85,000) / $15,000
- MFJ: (Modified AGI - $170,000) / $30,000

MFS: NOT eligible for deduction.

================================================================================
LO 6-2: DEDUCTIONS FROM AGI - ITEMIZED DEDUCTIONS
================================================================================

Itemized deductions include personal expenses allowed to subsidize desirable activities (home ownership, charitable giving) or provide relief for involuntary reduction in ability to pay (medical expenses).

---

**MEDICAL EXPENSES**

Designed to provide relief for taxpayers whose ability to pay is seriously hindered by health circumstances.

Qualified medical expenses include:
- Care, prevention, diagnosis, or cure of injury, disease, or bodily function
- Not reimbursed by insurance or paid through FSA/HSA
- For taxpayer, spouse, and dependents

Common medical expenses:
- Prescription medication, insulin, medical aids (eyeglasses, wheelchairs)
- Payments to medical providers and facilities
- Transportation for medical purposes (21 cents/mile in 2025)
- Long-term care facilities
- Health insurance premiums (if not deducted for AGI)
- Long-term care insurance

NOT deductible: Cosmetic surgery (unless for congenital abnormality, injury/accident, or disfiguring disease); over-the-counter medicines.

**Medical Expense Deduction Limitation:**
Deductible amount = Unreimbursed qualified medical expenses - 7.5% of AGI

This is a FLOOR limitation (eliminates deduction for amounts below the floor).

---

**TAXES**

Deductible taxes:
- State and local income taxes (or sales taxes, by election)
- State and local real estate taxes (personal or investment property)
- State and local personal property taxes (based on value of property)

**OBBBA SALT Limitation (2025):**
Total state and local tax deduction limited to $40,000 ($20,000 for MFS).
Foreign income taxes are NOT subject to this limit.

**Phase-out of SALT cap:**
Cap reduced by 30% of (modified AGI - $500,000).
- $500,000 threshold ($250,000 for MFS)
- Cap cannot go below $10,000 ($5,000 for MFS)

---

**INTEREST**

Two types of deductible interest:

**1. Home Mortgage Interest:**
Deductible on acquisition indebtedness secured by qualified residence (principal residence + one other).

Acquisition indebtedness: Debt incurred to acquire, construct, or substantially improve the residence.

Limits on acquisition indebtedness:
- Post-December 15, 2017 debt: $750,000 ($375,000 MFS)
- Pre-December 16, 2017 debt: $1,000,000 ($500,000 MFS)

**2. Investment Interest:**
Interest on loans to purchase investment assets (stocks, bonds, land).
Limited to net investment income. Excess carries forward.

NOT deductible: Personal credit card interest; personal auto loan interest (but see OBBBA car loan interest deduction below).

---

**CHARITABLE CONTRIBUTIONS**

Deductible contributions to qualified domestic charitable organizations (educational, religious, scientific, governmental, public activities).

NOT deductible: Political/campaign contributions.

**Contributions of Money:**
Cash, check, electronic transfer, credit card, payroll deduction.
Transportation for charity: 14 cents/mile.
Services provided to charity: NOT deductible (but out-of-pocket expenses are).

If receiving goods/services in exchange: Deduct only amount exceeding FMV of goods/services received.

**Contributions of Property:**

*Capital Gain Property:*
- Held more than one year
- Would generate long-term capital gain if sold
- Includes investment assets, business assets, personal-use assets
- Deduct FMV (generally)

Exception: Tangible personal property used for unrelated purpose by charity → deduct basis only.

*Ordinary Income Property:*
- Assets held one year or less
- Inventory
- Depreciation recapture property
- Assets that have declined in value
- Deduct lesser of FMV or basis

**Charitable Contribution AGI Limitations:**

EXHIBIT 6-9: Charitable Contribution Limits

| Contribution Type | Public Charity | Private Nonoperating Foundation |
|-------------------|----------------|--------------------------------|
| Cash | 60% of AGI | 30% of AGI |
| Capital gain property | 30% of AGI (FMV) | 20% of AGI (basis)* |
| Ordinary income property | 50% of AGI (lesser of FMV or basis) | 30% of AGI |

*FMV if publicly traded stock.

Order of applying limitations:
1. 60% contributions
2. 50% contributions
3. 30% contributions
4. 20% contributions

Excess contributions carry forward 5 years.

---

**CASUALTY AND THEFT LOSSES ON PERSONAL-USE ASSETS**

Generally NOT deductible.

Exception: Losses attributable to federally declared disaster.
- $100 floor per casualty
- 10% of AGI floor for all casualties

---

**OTHER ITEMIZED DEDUCTIONS**

NOT deductible after 2017:
- Employee business expenses
- Tax preparation fees
- Investment expenses (other than investment interest)
- Hobby expenses

KEY FACTS: Other Itemized Deductions
- Employee expenses, tax prep fees, investment expenses, hobby expenses: NOT deductible
- Gambling losses: Deductible to extent of gambling winnings (as itemized deduction)

Still deductible:
- Gambling losses (to extent of winnings)
- Casualty/theft losses on investment property
- Unrecovered cost of life annuity (if taxpayer died before full recovery)

================================================================================
LO 6-3: THE STANDARD DEDUCTION
================================================================================

Taxpayers deduct the GREATER of standard deduction or itemized deductions.

Standard deduction varies by filing status, age, and eyesight.

EXHIBIT 6-11: Standard Deduction Amounts

**2024:**
| Filing Status | Basic | Additional (Age 65+/Blind) |
|---------------|-------|---------------------------|
| MFJ/QSS | $29,200 | $1,550 |
| HoH | $21,900 | $1,950 |
| Single | $14,600 | $1,950 |
| MFS | $14,600 | $1,550 |

**2025:**
| Filing Status | Basic | Additional (Age 65+/Blind) |
|---------------|-------|---------------------------|
| MFJ/QSS | $31,500 | $1,600 |
| HoH | $23,625 | $2,000 |
| Single | $15,750 | $2,000 |
| MFS | $15,750 | $1,600 |

Additional standard deduction: One for age 65+, one for blind (can get both).

**Dependents' Standard Deduction:**
Greater of:
1. $1,350, OR
2. $450 + earned income (not to exceed regular standard deduction)

Additional amounts for age/blindness still apply to dependents.

**Bunching Strategy:**
Shift itemized deductions into one year to exceed standard deduction, then take standard deduction in alternate years. Works well for charitable contributions.

================================================================================
LO 6-4: OTHER FROM AGI DEDUCTIONS
================================================================================

Five from AGI deductions available regardless of itemizing or taking standard deduction:
1. Qualified Business Income (QBI) deduction
2. Qualified Tip Income deduction (OBBBA)
3. Qualified Overtime Compensation deduction (OBBBA)
4. Qualified Car Loan Interest deduction (OBBBA)
5. Deduction for Seniors (OBBBA)

---

**DEDUCTION FOR QUALIFIED BUSINESS INCOME (QBI)**

KEY FACTS: QBI Deduction
- From AGI deduction in ADDITION to standard/itemized deductions
- Limited to qualified trades or businesses
- Subject to multiple limitations

Deduction = Lesser of:
1. 20% of QBI from qualified trade or business (after wage limit) + 20% of qualified REIT dividends and qualified PTP income, OR
2. 20% of (taxable income - net capital gains including qualified dividends)

**Qualified Trade or Business:**
Any trade or business EXCEPT:
- Specified service trade or business (SSTB)
- Trade or business of being an employee

**Specified Service Trade or Business (SSTB):**
Services in: health, law, consulting, accounting, actuarial science, performing arts, athletics, financial services, brokerage services.
Also: Any business where principal asset is reputation/skill of employees/owners.
Also: Investing, investment management, trading in securities/commodities.

NOT SSTB: Architecture and engineering (always qualify for QBI deduction).

Rental activities: May qualify if considered trade or business based on facts and circumstances.

**Income Thresholds for SSTB Exclusion:**

If taxable income (before QBI deduction) is:
- Below $197,300 ($394,600 MFJ; $197,300 MFS): SSTB exclusion doesn't apply (business qualifies)
- Above $247,300 ($494,600 MFJ; $247,300 MFS): SSTB fully excluded (no QBI deduction for that business)
- Between thresholds: Phase-in over $50,000 range ($100,000 MFJ)

**Qualified Business Income:**
Net qualified items of income, gain, deduction, and loss from qualified trade or business in the United States.

NOT included: Capital gains/losses, dividends, interest not allocable to trade or business, tip income deducted as qualified tip income.

Reduced by: Deductible portion of SE taxes, self-employed health insurance deduction, contributions to qualified self-employed retirement plans.

If QBI is a loss: Carries forward to next year.

**Wage-Based Limitation:**
QBI deduction cannot exceed GREATER of:
1. 50% of wages paid, OR
2. 25% of wages + 2.5% of unadjusted basis of qualified property

Wage limit applies separately to each qualified trade or business.

**When Wage Limit Applies:**
- Taxable income below $197,300 ($394,600 MFJ): Wage limit does NOT apply
- Taxable income above $247,300 ($494,600 MFJ): Wage limit fully applies
- Between thresholds: Wage limit phases in over $50,000 range ($100,000 MFJ)

---

**DEDUCTION FOR QUALIFIED TIP INCOME (OBBBA 2025-2028)**

Deduct up to $25,000 of qualified tips properly reported.

Qualified tips:
- Cash tips in occupation where tipping was customary before January 1, 2025
- Voluntary, not negotiated
- NOT received in SSTB

Phase-out: Reduced by $100 for every $1,000 of modified AGI over $150,000 ($300,000 MFJ).
Fully phased out at $400,000 AGI ($550,000 MFJ).

Must file MFJ if married (not available for MFS).

---

**DEDUCTION FOR QUALIFIED OVERTIME COMPENSATION (OBBBA 2025-2028)**

Deduct up to $12,500 ($25,000 MFJ) of qualified overtime compensation properly reported on W-2 or 1099.

Qualified overtime: Overtime required under Fair Labor Standards Act (hours beyond 40/week).
Does NOT include qualified tip income.

Phase-out: Reduced by $100 for every $1,000 of modified AGI over $150,000 ($300,000 MFJ).
Fully phased out at $275,000 AGI ($550,000 MFJ).

Must file MFJ if married (not available for MFS).

---

**DEDUCTION FOR QUALIFIED CAR LOAN INTEREST (OBBBA 2025-2028)**

Deduct up to $10,000 of qualified car loan interest per year.

Requirements:
- Debt incurred after December 31, 2024
- For purchase of new personal use vehicle (car, minivan, SUV, pickup, motorcycle under 14,000 lbs)
- Final assembly in United States
- Must report VIN on tax return
- Lender must file information return with IRS
- Vehicle's original use must begin with taxpayer

Phase-out: Reduced by $200 for every $1,000 (or portion) of modified AGI over $100,000 ($200,000 MFJ).
Fully phased out at $149,001 AGI ($249,001 MFJ).

---

**DEDUCTION FOR SENIORS (OBBBA 2025-2028)**

$6,000 deduction for taxpayers age 65+ at year-end.
$6,000 additional for spouse age 65+ (MFJ only).

Must file MFJ if married (not available for MFS).

Phase-out: Reduced by 6% of (modified AGI - $75,000).
- $75,000 threshold ($150,000 MFJ)
- Fully phased out at $175,000 ($250,000 MFJ with one 65+; $350,000 MFJ with both 65+)

================================================================================
SUMMARY: TAXABLE INCOME CALCULATION
================================================================================

1. Gross Income (all income from whatever source derived, unless excluded)

2. Minus: For AGI Deductions
   - Business expenses (Schedule C)
   - Rental/royalty expenses (Schedule E)
   - Capital losses (up to $3,000)
   - Self-employment tax (50%)
   - Self-employed health insurance
   - IRA contributions
   - HSA contributions
   - Student loan interest (up to $2,500)
   - Alimony paid (pre-2019 agreements)
   - Early withdrawal penalties

3. Equals: Adjusted Gross Income (AGI)

4. Minus: From AGI Deductions
   - Greater of:
     a. Standard deduction, OR
     b. Itemized deductions (medical, taxes, interest, charity, other)
   - PLUS (regardless of itemizing):
     - QBI deduction (20% of qualified business income)
     - Senior deduction ($6,000 if 65+)
     - Qualified car loan interest (up to $10,000)
     - Qualified tip income (up to $25,000)
     - Qualified overtime (up to $12,500/$25,000)

5. Equals: TAXABLE INCOME

================================================================================
=== END OF ACC 405 TAX TEXTBOOK CONTENT ===
================================================================================
"""


# ============================================================================
# CUSTOM CSS - DARK MODE THEME
# ============================================================================
st.markdown("""
    <style>
    /* ===== GLOBAL STYLES ===== */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    header[data-testid="stHeader"] {
        background-color: #0E1117 !important;
    }
    
    .stApp {
        font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* ===== TEXT COLORS ===== */
    .stApp, .stMarkdown, p, span, div, label, li, td, th {
        color: #FFFFFF !important;
    }
    
    code {
        color: #FFFFFF !important;
        background-color: #1E1E1E !important;
    }
    
    .stCodeBlock, pre {
        background-color: #1E1E1E !important;
    }
    
    /* ===== SIDEBAR STYLING ===== */
    section[data-testid="stSidebar"] {
        background-color: #0A0A0F !important;
        border-right: 1px solid #1E1E1E !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #0A0A0F !important;
    }
    
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    section[data-testid="stSidebar"] h1 {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
    }
    
    /* ===== ALL BUTTONS - GOLD WITH WHITE TEXT ===== */
    .stButton > button {
        background: linear-gradient(145deg, #CFB53B, #B8A033) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border: none !important;
        font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(207, 181, 59, 0.2) !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(145deg, #E0C64C, #CFB53B) !important;
        color: #FFFFFF !important;
        box-shadow: 0 6px 20px rgba(207, 181, 59, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button p {
        color: #FFFFFF !important;
    }
    
    /* Download buttons */
    .stDownloadButton > button {
        background: linear-gradient(145deg, #CFB53B, #B8A033) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(207, 181, 59, 0.2) !important;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(145deg, #E0C64C, #CFB53B) !important;
        transform: translateY(-2px) !important;
    }
    
    .stDownloadButton > button p, .stDownloadButton > button span {
        color: #FFFFFF !important;
    }
    
    /* Form submit buttons */
    .stFormSubmitButton > button {
        background: linear-gradient(145deg, #CFB53B, #B8A033) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(207, 181, 59, 0.2) !important;
    }
    
    .stFormSubmitButton > button:hover {
        background: linear-gradient(145deg, #E0C64C, #CFB53B) !important;
        transform: translateY(-2px) !important;
    }
    
    .stFormSubmitButton > button p {
        color: #FFFFFF !important;
    }
    
    /* ===== EXPANDERS ===== */
    [data-testid="stExpander"] {
        background-color: #1A1A2E !important;
        border: 1px solid #2D2D4A !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    
    [data-testid="stExpander"] > details > summary {
        background-color: #1A1A2E !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 15px 20px !important;
        font-weight: 500 !important;
    }
    
    [data-testid="stExpander"] > details > summary:hover,
    [data-testid="stExpander"] > details > summary:focus,
    [data-testid="stExpander"] > details > summary:active,
    [data-testid="stExpander"] > details[open] > summary {
        background-color: #252542 !important;
        color: #FFFFFF !important;
    }
    
    [data-testid="stExpander"] > details > summary p,
    [data-testid="stExpander"] > details > summary span,
    [data-testid="stExpander"] > details > summary svg {
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }
    
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
        background-color: #12121F !important;
        border-top: 1px solid #2D2D4A !important;
        padding: 20px !important;
    }
    
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] p,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] span,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] div,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] li,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] strong,
    [data-testid="stExpander"] div[data-testid="stExpanderDetails"] em {
        color: #FFFFFF !important;
    }
    
    .streamlit-expanderHeader {
        background-color: #1A1A2E !important;
        color: #FFFFFF !important;
    }
    
    .streamlit-expanderHeader:hover,
    .streamlit-expanderHeader:focus,
    .streamlit-expanderHeader:active {
        background-color: #252542 !important;
        color: #FFFFFF !important;
    }
    
    .streamlit-expanderHeader p, 
    .streamlit-expanderHeader span {
        color: #FFFFFF !important;
    }
    
    .streamlit-expanderContent {
        background-color: #12121F !important;
        border: 1px solid #2D2D4A !important;
    }
    
    .streamlit-expanderContent * {
        color: #FFFFFF !important;
    }
    
    /* ===== INPUT FIELDS ===== */
    .stTextInput > div > div > input {
        background-color: #1A1A2E !important;
        color: #FFFFFF !important;
        border: 1px solid #2D2D4A !important;
        border-radius: 10px !important;
        padding: 12px 15px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #CFB53B !important;
        box-shadow: 0 0 0 2px rgba(207, 181, 59, 0.2) !important;
    }
    
    .stTextInput label {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    /* Text areas - WHITE background for readability */
    .stTextArea > div > div > textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #2D2D4A !important;
        border-radius: 10px !important;
        padding: 12px 15px !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #CFB53B !important;
        box-shadow: 0 0 0 2px rgba(207, 181, 59, 0.2) !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: #666666 !important;
    }
    
    .stTextArea label {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    /* Number inputs */
    .stNumberInput > div > div > input {
        background-color: #1A1A2E !important;
        color: #FFFFFF !important;
        border: 1px solid #2D2D4A !important;
        border-radius: 10px !important;
        padding: 12px 15px !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #CFB53B !important;
    }
    
    .stNumberInput label {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    /* Select boxes / dropdowns */
    .stSelectbox > div > div {
        background-color: #1A1A2E !important;
        color: #FFFFFF !important;
        border: 1px solid #2D2D4A !important;
        border-radius: 10px !important;
    }
    
    .stSelectbox label {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    .stSelectbox > div > div > div {
        color: #FFFFFF !important;
    }
    
    [data-baseweb="menu"] {
        background-color: #1A1A2E !important;
        border: 1px solid #2D2D4A !important;
        border-radius: 10px !important;
    }
    
    [data-baseweb="menu"] li {
        color: #FFFFFF !important;
        background-color: #1A1A2E !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background-color: #252542 !important;
    }
    
    /* ===== RADIO BUTTONS ===== */
    .stRadio > div {
        background-color: transparent !important;
    }
    
    .stRadio label {
        color: #FFFFFF !important;
    }
    
    .stRadio > div > label > div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important;
    }
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: 10px;
        border-bottom: 1px solid #2D2D4A !important;
        padding-bottom: 0 !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        color: #888888 !important;
        border-radius: 10px 10px 0 0 !important;
        border: none !important;
        padding: 15px 25px !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #1A1A2E !important;
        color: #FFFFFF !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #002E5D !important;
        color: #FFFFFF !important;
        border-bottom: 3px solid #CFB53B !important;
    }
    
    .stTabs [data-baseweb="tab-panel"] {
        background-color: transparent !important;
        padding-top: 30px !important;
    }
    
    /* ===== INFO/SUCCESS/WARNING/ERROR BOXES ===== */
    .stAlert {
        background-color: #1A1A2E !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        border: 1px solid #2D2D4A !important;
    }
    
    .stAlert p, .stAlert span, .stAlert div {
        color: #FFFFFF !important;
    }
    
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentInfo"]) {
        background-color: #1E3A5F !important;
        border-left: 4px solid #4A90D9 !important;
    }
    
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentSuccess"]) {
        background-color: #1E3E1E !important;
        border-left: 4px solid #4CAF50 !important;
    }
    
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentWarning"]) {
        background-color: #3E3A1E !important;
        border-left: 4px solid #FFC107 !important;
    }
    
    [data-testid="stAlert"][data-baseweb="notification"]:has(div[data-testid="stNotificationContentError"]) {
        background-color: #3E1E1E !important;
        border-left: 4px solid #F44336 !important;
    }
    
    /* ===== SPINNER ===== */
    .stSpinner > div {
        color: #FFFFFF !important;
    }
    
    /* ===== CAPTION TEXT ===== */
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #AAAAAA !important;
    }
    
    .stCaption p {
        color: #AAAAAA !important;
    }
    
    /* ===== CHAT STYLING ===== */
    .user-message {
        background: linear-gradient(145deg, #1E3A5F, #162D4A);
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        border: 1px solid #2D4A6F;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .user-message strong, .user-message br, .user-message * {
        color: #FFFFFF !important;
    }
    
    .ai-message {
        background: linear-gradient(145deg, #1A1A2E, #151525);
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        border-left: 4px solid #CFB53B;
        border-top: 1px solid #2D2D4A;
        border-right: 1px solid #2D2D4A;
        border-bottom: 1px solid #2D2D4A;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .ai-message strong, .ai-message * {
        color: #FFFFFF !important;
    }
    
    /* ===== PLOTLY CHARTS ===== */
    .js-plotly-plot .plotly .modebar {
        background-color: transparent !important;
    }
    
    .js-plotly-plot .plotly .modebar-btn path {
        fill: #FFFFFF !important;
    }
    
    /* ===== HORIZONTAL RULE ===== */
    hr {
        border-color: #2D2D4A !important;
    }
    
    /* ===== LINKS ===== */
    a {
        color: #CFB53B !important;
    }
    
    a:hover {
        color: #E8D066 !important;
    }
    
    /* ===== SCROLLBAR STYLING ===== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0E1117;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #2D2D4A;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #3D3D5A;
    }
    
    /* ===== MARKDOWN SPECIFIC ===== */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #FFFFFF !important;
    }
    
    /* ===== PAGE HEADERS ===== */
    .page-header {
        text-align: center;
        padding: 40px 20px;
        margin-bottom: 30px;
        background: linear-gradient(180deg, #0E1117 0%, #1A1A2E 100%);
        border-radius: 0 0 20px 20px;
        border-bottom: 1px solid #2D2D4A;
    }
    
    .page-header h1 {
        color: #FFFFFF !important;
        font-size: 2.5em !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        margin-bottom: 10px !important;
    }
    
    .page-header p {
        color: #888888 !important;
        font-size: 1.1em !important;
    }
    
    /* ===== CARD STYLING ===== */
    .pro-card {
        background: linear-gradient(145deg, #1A1A2E, #151525);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #2D2D4A;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }
    
    .pro-card-blue {
        background: linear-gradient(145deg, #002E5D, #001A3A);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #003D7A;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; margin-bottom: 30px; padding-top: 10px;'>
            <svg width="140" height="140" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">
                <circle cx="110" cy="110" r="105" fill="#002E5D"/>
                <text x="110" y="85" font-size="48" fill="white" text-anchor="middle" font-weight="bold" font-family="Arial, sans-serif">BYU</text>
                <text x="110" y="115" font-size="14" fill="#CFB53B" text-anchor="middle" font-family="Arial, sans-serif" letter-spacing="3">MARRIOTT SCHOOL</text>
                <line x1="60" y1="130" x2="160" y2="130" stroke="#CFB53B" stroke-width="1" opacity="0.6"/>
                <text x="110" y="155" font-size="18" fill="white" text-anchor="middle" font-family="Arial, sans-serif" letter-spacing="4">ACCOUNTING</text>
            </svg>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; color: #CFB53B; font-size: 0.9em; letter-spacing: 2px; margin-bottom: 30px;'>
            STUDY HUB
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    pages = [
        "🏠 Home",
        "🧮 Calculators",
        "📖 Formula Database",
        "📊 Break-Even Visualizer",
        "📕 ACC 402 - Managerial Accounting",
        "📗 ACC 405 - Tax Accounting"
    ]
    
    for page_name in pages:
        if st.button(page_name, key=f"nav_{page_name}", use_container_width=True):
            st.session_state.selected_page = page_name
            st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <p style='color: #666666; font-size: 0.8em; margin-bottom: 5px;'>Created for</p>
            <p style='color: #FFFFFF; font-size: 0.9em; font-weight: 500;'>BYU Accounting Students</p>
            <p style='color: #CFB53B; font-size: 0.75em; margin-top: 10px;'>AI & Data Analytics</p>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN CONTENT AREA
# ============================================================================

page = st.session_state.selected_page

# --- PAGE 1: HOME ---
if page == "🏠 Home":
    # Scroll to top
    st.components.v1.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; padding: 40px 20px 40px 20px;'>
            <div style='margin-bottom: 40px;'>
                <svg width="220" height="220" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="110" cy="110" r="105" fill="#002E5D"/>
                    <text x="110" y="85" font-size="48" fill="white" text-anchor="middle" font-weight="bold" font-family="Arial, sans-serif">BYU</text>
                    <text x="110" y="115" font-size="14" fill="#CFB53B" text-anchor="middle" font-family="Arial, sans-serif" letter-spacing="3">MARRIOTT SCHOOL</text>
                    <line x1="60" y1="130" x2="160" y2="130" stroke="#CFB53B" stroke-width="1" opacity="0.6"/>
                    <text x="110" y="155" font-size="18" fill="white" text-anchor="middle" font-family="Arial, sans-serif" letter-spacing="4">ACCOUNTING</text>
                    <text x="110" y="178" font-size="12" fill="#AAAAAA" text-anchor="middle" font-family="Arial, sans-serif" letter-spacing="2">STUDY HUB</text>
                </svg>
            </div>
            <h1 style='color: #FFFFFF; font-size: 3.2em; margin-bottom: 15px; font-weight: 700; letter-spacing: 2px;'>
                Accounting Study Hub
            </h1>
            <p style='color: #CFB53B; font-size: 1.1em; margin-top: 0; font-weight: 600; letter-spacing: 4px; text-transform: uppercase;'>
                Brigham Young University
            </p>
            <p style='color: #888888; font-size: 1em; margin-top: 25px; max-width: 550px; margin-left: auto; margin-right: auto; line-height: 1.7;'>
                AI-powered study tools designed to help you master managerial accounting concepts and ace your exams.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='display: flex; align-items: center; justify-content: center; margin: 40px 0;'>
            <div style='flex: 1; height: 1px; background: linear-gradient(to right, transparent, #2D2D4A, transparent);'></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style='text-align: center; color: #FFFFFF; font-weight: 400; letter-spacing: 1px; margin-bottom: 40px;'>
            Get Started
        </h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #002E5D, #001A3A);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #003D7A;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            height: 100%;
        '>
            <div style='font-size: 2.5em; margin-bottom: 15px;'>📕</div>
            <h3 style='color: #FFFFFF; margin-bottom: 10px; font-size: 1.4em; font-weight: 500;'>
                ACC 402
            </h3>
            <p style='color: #CFB53B; font-size: 0.9em; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;'>
                Managerial Accounting
            </p>
            <p style='color: #AAAAAA; font-size: 0.95em; line-height: 1.6;'>
                AI Tutor with full textbook access covering Chapters 1, 3, 4, 6, and 7. Get instant help with concepts, formulas, and practice problems.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Launch ACC 402 →", key="goto_402", use_container_width=True):
            st.session_state.selected_page = "📕 ACC 402 - Managerial Accounting"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #1B5E20, #0D3D12);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #2E7D32;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            height: 100%;
        '>
            <div style='font-size: 2.5em; margin-bottom: 15px;'>📗</div>
            <h3 style='color: #FFFFFF; margin-bottom: 10px; font-size: 1.4em; font-weight: 500;'>
                ACC 405
            </h3>
            <p style='color: #81C784; font-size: 0.9em; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;'>
                Tax Accounting
            </p>
            <p style='color: #AAAAAA; font-size: 0.95em; line-height: 1.6;'>
                AI Tutor with full tax textbook access. Get help with tax concepts, calculations, and filing requirements.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Launch ACC 405 →", key="goto_405", use_container_width=True):
            st.session_state.selected_page = "📗 ACC 405 - Tax Accounting"
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col3, col4 = st.columns(2, gap="large")
    
    with col3:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #1A1A2E, #151525);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #2D2D4A;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            height: 100%;
        '>
            <div style='font-size: 2.5em; margin-bottom: 15px;'>🧮</div>
            <h3 style='color: #FFFFFF; margin-bottom: 10px; font-size: 1.4em; font-weight: 500;'>
                Calculators
            </h3>
            <p style='color: #CFB53B; font-size: 0.9em; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;'>
                Quick Tools
            </p>
            <p style='color: #AAAAAA; font-size: 0.95em; line-height: 1.6;'>
                Contribution margin, break-even analysis, overhead rates, and more. Get instant answers to common accounting calculations.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Open Calculators →", key="goto_calc", use_container_width=True):
            st.session_state.selected_page = "🧮 Calculators"
            st.rerun()
    
    with col4:
        st.markdown("""
        <div style='
            background: linear-gradient(145deg, #1A1A2E, #151525);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #2D2D4A;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            height: 100%;
        '>
            <div style='font-size: 2.5em; margin-bottom: 15px;'>📖</div>
            <h3 style='color: #FFFFFF; margin-bottom: 10px; font-size: 1.4em; font-weight: 500;'>
                Formula Database
            </h3>
            <p style='color: #CFB53B; font-size: 0.9em; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;'>
                Quick Reference
            </p>
            <p style='color: #AAAAAA; font-size: 0.95em; line-height: 1.6;'>
                Searchable database of key accounting formulas. Find exactly what you need for homework and exams.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Browse Formulas →", key="goto_formulas", use_container_width=True):
            st.session_state.selected_page = "📖 Formula Database"
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; padding: 30px 20px; border-top: 1px solid #2D2D4A;'>
            <p style='color: #555; font-size: 0.85em;'>
                Built with AI & Data Analytics • BYU Marriott School of Business
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE 2: CALCULATORS ---
elif page == "🧮 Calculators":
    # Scroll to top
    st.components.v1.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )
    
    st.markdown("""
        <div class='page-header'>
            <h1>🧮 Accounting Calculators</h1>
            <p>Quick calculation tools for common accounting problems</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_calc"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    calc_type = st.selectbox(
        "Choose a calculator:",
        ["Contribution Margin", "Break-Even Point (Units)", "Break-Even Point (Dollars)", 
         "Target Profit", "Overhead Rate"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='
            background: linear-gradient(145deg, #1A1A2E, #151525);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #2D2D4A;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
        '>
    """, unsafe_allow_html=True)
    
    if calc_type == "Contribution Margin":
        st.subheader("Contribution Margin Calculator")
        st.markdown("<p style='color: #888888; margin-bottom: 20px;'>Calculate the amount available to cover fixed costs and generate profit.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            sales = st.number_input("Sales ($)", min_value=0.0, value=100000.0, step=1000.0)
        with col2:
            var_costs = st.number_input("Variable Costs ($)", min_value=0.0, value=60000.0, step=1000.0)
        
        if st.button("Calculate", key="cm_calc"):
            cm = sales - var_costs
            cm_ratio = (cm / sales * 100) if sales > 0 else 0
            
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"**Contribution Margin:** ${cm:,.2f}")
            with col2:
                st.success(f"**CM Ratio:** {cm_ratio:.2f}%")
    
    elif calc_type == "Break-Even Point (Units)":
        st.subheader("Break-Even Point (Units)")
        st.markdown("<p style='color: #888888; margin-bottom: 20px;'>Calculate the number of units needed to cover all costs.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            fixed = st.number_input("Fixed Costs ($)", min_value=0.0, value=30000.0, step=1000.0)
        with col2:
            cm_unit = st.number_input("CM per Unit ($)", min_value=0.01, value=15.0, step=1.0)
        
        if st.button("Calculate", key="bep_units"):
            bep = fixed / cm_unit
            st.markdown("<br>", unsafe_allow_html=True)
            st.success(f"**Break-Even Point:** {bep:,.0f} units")
    
    elif calc_type == "Break-Even Point (Dollars)":
        st.subheader("Break-Even Point (Dollars)")
        st.markdown("<p style='color: #888888; margin-bottom: 20px;'>Calculate the sales dollars needed to break even.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            fixed = st.number_input("Fixed Costs ($)", min_value=0.0, value=30000.0, step=1000.0)
        with col2:
            cm_ratio = st.number_input("CM Ratio (%)", min_value=0.01, max_value=100.0, value=40.0, step=1.0)
        
        if st.button("Calculate", key="bep_dollars"):
            bep = fixed / (cm_ratio / 100)
            st.markdown("<br>", unsafe_allow_html=True)
            st.success(f"**Break-Even Point:** ${bep:,.2f}")
    
    elif calc_type == "Target Profit":
        st.subheader("Target Profit Calculator")
        st.markdown("<p style='color: #888888; margin-bottom: 20px;'>Calculate units needed to achieve a target profit.</p>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            fixed = st.number_input("Fixed Costs ($)", min_value=0.0, value=30000.0, step=1000.0)
        with col2:
            target = st.number_input("Target Profit ($)", min_value=0.0, value=20000.0, step=1000.0)
        with col3:
            cm_unit = st.number_input("CM per Unit ($)", min_value=0.01, value=15.0, step=1.0)
        
        if st.button("Calculate", key="target_profit"):
            units = (fixed + target) / cm_unit
            st.markdown("<br>", unsafe_allow_html=True)
            st.success(f"**Units Needed:** {units:,.0f} units")
    
    elif calc_type == "Overhead Rate":
        st.subheader("Predetermined Overhead Rate")
        st.markdown("<p style='color: #888888; margin-bottom: 20px;'>Calculate the rate used to apply overhead to jobs.</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            est_oh = st.number_input("Estimated Overhead ($)", min_value=0.0, value=100000.0, step=1000.0)
        with col2:
            est_activity = st.number_input("Estimated Activity (hours)", min_value=1.0, value=20000.0, step=100.0)
        
        if st.button("Calculate", key="oh_rate"):
            rate = est_oh / est_activity
            st.markdown("<br>", unsafe_allow_html=True)
            st.success(f"**Overhead Rate:** ${rate:.2f} per hour")
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 3: FORMULA DATABASE ---
elif page == "📖 Formula Database":
    # Scroll to top
    st.components.v1.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )
    
    st.markdown("""
        <div class='page-header'>
            <h1>📖 Formula Database</h1>
            <p>Quick reference for key accounting formulas</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_formula"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    search = st.text_input("🔍 Search formulas (e.g., 'contribution', 'overhead', 'cost')")
    
    formulas = {
        "Contribution Margin": {
            "formula": "Sales - Variable Costs",
            "description": "Amount available to cover fixed costs and profit"
        },
        "Contribution Margin Ratio": {
            "formula": "Contribution Margin ÷ Sales",
            "description": "Percentage of each sales dollar available for fixed costs"
        },
        "Break-Even Point (Units)": {
            "formula": "Fixed Costs ÷ CM per Unit",
            "description": "Number of units needed to cover all costs"
        },
        "Break-Even Point (Dollars)": {
            "formula": "Fixed Costs ÷ CM Ratio",
            "description": "Sales dollars needed to break even"
        },
        "Target Profit (Units)": {
            "formula": "(Fixed Costs + Target Profit) ÷ CM per Unit",
            "description": "Units needed to achieve desired profit"
        },
        "Predetermined Overhead Rate": {
            "formula": "Estimated Overhead ÷ Estimated Activity",
            "description": "Rate used to apply overhead to jobs"
        },
        "Applied Overhead": {
            "formula": "Predetermined Rate × Actual Activity",
            "description": "Overhead allocated to a specific job"
        },
        "Prime Costs": {
            "formula": "Direct Materials + Direct Labor",
            "description": "Direct costs of production"
        },
        "Conversion Costs": {
            "formula": "Direct Labor + Factory Overhead",
            "description": "Costs to convert materials into finished goods"
        },
        "Cost of Goods Manufactured": {
            "formula": "Beginning WIP + Manufacturing Costs - Ending WIP",
            "description": "Total cost of units completed in production"
        },
        "Cost of Goods Sold": {
            "formula": "Beginning FG + COGM - Ending FG",
            "description": "Cost of inventory sold during the period"
        },
        "Equivalent Units (Weighted-Average)": {
            "formula": "Units Completed + (Ending WIP × % Complete)",
            "description": "Measures work done in a period"
        },
        "Equivalent Units (FIFO)": {
            "formula": "Work to Complete Beg. WIP + Started & Completed + (Ending WIP × % Complete)",
            "description": "Measures current period work only"
        }
    }
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if search:
        filtered = {k: v for k, v in formulas.items() if search.lower() in k.lower()}
        if filtered:
            for name, data in filtered.items():
                with st.expander(f"📐 {name}"):
                    st.markdown(f"**Formula:**")
                    st.code(data["formula"], language=None)
                    st.markdown(f"*{data['description']}*")
        else:
            st.warning("No formulas found. Try a different search term.")
    else:
        for name, data in formulas.items():
            with st.expander(f"📐 {name}"):
                st.markdown(f"**Formula:**")
                st.code(data["formula"], language=None)
                st.markdown(f"*{data['description']}*")

# --- PAGE 4: BREAK-EVEN VISUALIZER ---
elif page == "📊 Break-Even Visualizer":
    # Scroll to top
    st.components.v1.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )
    
    st.markdown("""
        <div class='page-header'>
            <h1>📊 Break-Even Visualizer</h1>
            <p>Interactive cost-volume-profit analysis</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_viz"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='
            background: linear-gradient(145deg, #1A1A2E, #151525);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #2D2D4A;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            margin-bottom: 30px;
        '>
            <h3 style='color: #FFFFFF; margin-bottom: 20px;'>Enter Your Data</h3>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        price = st.number_input("Selling Price per Unit ($)", min_value=0.01, value=50.0, step=1.0)
        var_cost = st.number_input("Variable Cost per Unit ($)", min_value=0.0, value=30.0, step=1.0)
    
    with col2:
        fixed_costs = st.number_input("Total Fixed Costs ($)", min_value=0.0, value=40000.0, step=1000.0)
        max_units = st.number_input("Max Units to Display", min_value=100, value=5000, step=100)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Generate Chart", key="gen_chart", use_container_width=True):
        units = list(range(0, max_units + 1, 100))
        revenue = [price * u for u in units]
        total_cost = [fixed_costs + (var_cost * u) for u in units]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(x=units, y=revenue, mode='lines', name='Revenue', 
                                 line=dict(color='#4CAF50', width=3)))
        fig.add_trace(go.Scatter(x=units, y=total_cost, mode='lines', name='Total Cost', 
                                 line=dict(color='#F44336', width=3)))
        
        bep_units = fixed_costs / (price - var_cost) if price > var_cost else 0
        bep_revenue = price * bep_units
        
        fig.add_trace(go.Scatter(x=[bep_units], y=[bep_revenue], mode='markers', 
                                 name='Break-Even Point',
                                 marker=dict(color='#CFB53B', size=15, symbol='diamond')))
        
        fig.update_layout(
            title=dict(text="Break-Even Analysis", font=dict(size=24, color='white')),
            xaxis_title="Units Sold",
            yaxis_title="Dollars ($)",
            hovermode='x unified',
            plot_bgcolor='#0E1117',
            paper_bgcolor='#0E1117',
            font=dict(color='white'),
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                font=dict(color='white')
            ),
            xaxis=dict(gridcolor='#2D2D4A', zerolinecolor='#2D2D4A'),
            yaxis=dict(gridcolor='#2D2D4A', zerolinecolor='#2D2D4A')
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
                <div style='background: linear-gradient(145deg, #002E5D, #001A3A); padding: 20px; border-radius: 12px; text-align: center;'>
                    <p style='color: #888; margin-bottom: 5px; font-size: 0.9em;'>Break-Even Units</p>
                    <p style='color: #FFFFFF; font-size: 1.8em; font-weight: 700; margin: 0;'>{bep_units:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div style='background: linear-gradient(145deg, #002E5D, #001A3A); padding: 20px; border-radius: 12px; text-align: center;'>
                    <p style='color: #888; margin-bottom: 5px; font-size: 0.9em;'>Break-Even Revenue</p>
                    <p style='color: #FFFFFF; font-size: 1.8em; font-weight: 700; margin: 0;'>${bep_revenue:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            cm_per_unit = price - var_cost
            st.markdown(f"""
                <div style='background: linear-gradient(145deg, #002E5D, #001A3A); padding: 20px; border-radius: 12px; text-align: center;'>
                    <p style='color: #888; margin-bottom: 5px; font-size: 0.9em;'>CM per Unit</p>
                    <p style='color: #FFFFFF; font-size: 1.8em; font-weight: 700; margin: 0;'>${cm_per_unit:,.2f}</p>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 5: ACC 402 AI TUTOR ---
elif page == "📕 ACC 402 - Managerial Accounting":
    # Scroll to top
    st.components.v1.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )
    
    st.markdown("""
        <div class='page-header'>
            <h1>📕 ACC 402 - Managerial Accounting</h1>
            <p>AI-powered study assistant with full textbook access</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_402"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🤖 AI Tutor", "📚 Key Formulas"])
    
    with tab1:
        st.markdown("""
            <div style='
                background: linear-gradient(145deg, #002E5D, #001A3A);
                padding: 25px;
                border-radius: 15px;
                border: 1px solid #003D7A;
                margin-bottom: 30px;
            '>
                <h3 style='color: #FFFFFF; margin-bottom: 10px;'>🤖 Your ACC 402 AI Study Assistant</h3>
                <p style='color: #AAAAAA; margin: 0;'>This AI tutor has <strong style='color: #CFB53B;'>word-for-word access</strong> to your full textbook (Chapters 1, 3, 4, 6, and 7). Ask anything!</p>
            </div>
        """, unsafe_allow_html=True)
        
        if 'trigger_ai_call' not in st.session_state:
            st.session_state.trigger_ai_call = False
        
        st.markdown("<p style='color: #FFFFFF; font-weight: 500; margin-bottom: 15px;'>📖 Quick Topics:</p>", unsafe_allow_html=True)
        topic_cols = st.columns(5)
        topics = [
            ("Ch 1", "Summarize the key concepts from Chapter 1 on Management Accounting"),
            ("Ch 3", "What are the key concepts from Chapter 3 on Basic Cost Management?"),
            ("Ch 4", "Explain job costing from Chapter 4"),
            ("Ch 6", "Walk me through process costing from Chapter 6"),
            ("Ch 7", "Explain cost allocation methods from Chapter 7")
        ]
        for idx, (label, question) in enumerate(topics):
            with topic_cols[idx]:
                if st.button(label, key=f"topic_{idx}", use_container_width=True):
                    st.session_state.chat_history_402.append({
                        'role': 'user',
                        'content': question
                    })
                    st.session_state.trigger_ai_call = True
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("⚙️ AI Settings"):
            model_choice = st.radio(
                "Model (Haiku is faster & cheaper, Sonnet is smarter):",
                ["claude-sonnet-4-20250514", "claude-haiku-3-5-20241022"],
                index=0,
                horizontal=True
            )
            st.caption("💡 Tip: Use Haiku for simple questions, Sonnet for complex explanations")
        
        if st.session_state.chat_history_402:
            for message in st.session_state.chat_history_402:
                if message['role'] == 'user':
                    st.markdown(f"""
                    <div class="user-message">
                        <strong>🧑‍🎓 You:</strong><br>{message['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="ai-message">
                        <strong>🤖 AI Tutor:</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(message['content'])
            st.markdown("<br>", unsafe_allow_html=True)
        
        if 'waiting_for_response' not in st.session_state:
            st.session_state.waiting_for_response = False
        
        with st.form(key="question_form_402", clear_on_submit=True):
            user_question = st.text_area(
                "Ask your question:", 
                height=100,
                placeholder="Example: What is the difference between job costing and process costing?",
                disabled=st.session_state.waiting_for_response
            )
            
            col1, col2 = st.columns([1, 5])
            with col1:
                submit_button = st.form_submit_button(
                    "Send" if not st.session_state.waiting_for_response else "Thinking...", 
                    type="primary",
                    disabled=st.session_state.waiting_for_response
                )
        
        btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 3])
        
        with btn_col1:
            if st.button("🗑️ Clear Chat", key="clear_chat_402"):
                st.session_state.chat_history_402 = []
                st.success("Chat cleared!")
                st.rerun()
        
        with btn_col2:
            if st.session_state.chat_history_402:
                chat_export = "\n\n".join([
                    f"{'You' if m['role'] == 'user' else 'AI Tutor'}: {m['content']}" 
                    for m in st.session_state.chat_history_402
                ])
                st.download_button(
                    "📥 Export Chat",
                    chat_export,
                    file_name="acc402_study_session.txt",
                    mime="text/plain"
                )
        
        should_call_api = False
        
        if submit_button and user_question.strip():
            st.session_state.chat_history_402.append({
                'role': 'user',
                'content': user_question
            })
            should_call_api = True
        
        if st.session_state.trigger_ai_call:
            should_call_api = True
            st.session_state.trigger_ai_call = False
        
        if should_call_api and st.session_state.chat_history_402:
            if st.session_state.chat_history_402[-1]['role'] == 'user':
                try:
                    api_key = st.secrets["ANTHROPIC_API_KEY"]
                    
                    system_prompt = f"""You are the Managerial Accounting Master Tutor, a specialized AI expert designed to help a junior-level accounting student master the material in their textbook.

Your goal is to provide clear, accurate, and exam-focused guidance based strictly on the textbook data provided below.

CORE RESPONSIBILITIES:
1. Knowledge Retrieval: Use the provided textbook content as your primary source of truth
2. Concept Simplification: Use the Feynman Technique - explain simply, then provide practical examples
3. Problem Solving: For math problems, walk through solutions step-by-step
4. Exam Prep: Create practice questions when asked

FORMATTING GUIDELINES:
- Use LaTeX for formulas (e.g., $$\\text{{BEP}} = \\frac{{\\text{{Fixed Costs}}}}{{\\text{{CM per Unit}}}}$$)
- Use bolding for key terms
- Use bullet points for lists
- Use tables for comparisons
- Be professional, encouraging, and academically rigorous

INTERACTION PROTOCOLS:
- If the student is confused, ask clarifying questions
- Check their work and point out errors
- Always cite which chapter/section you're referencing

{FULL_TEXTBOOK_CONTENT}

Now answer the student's question based on this textbook content."""
                    
                    with st.spinner("🤔 Thinking..."):
                        headers = {
                            "Content-Type": "application/json",
                            "x-api-key": api_key,
                            "anthropic-version": "2023-06-01"
                        }
                        
                        api_messages = []
                        for msg in st.session_state.chat_history_402:
                            api_messages.append({
                                "role": msg['role'],
                                "content": msg['content']
                            })
                        
                        data = {
                            "model": model_choice,
                            "max_tokens": 4096,
                            "system": system_prompt,
                            "messages": api_messages
                        }
                        
                        try:
                            response = requests.post(
                                "https://api.anthropic.com/v1/messages",
                                headers=headers,
                                json=data,
                                timeout=60
                            )
                            
                            if response.status_code == 200:
                                response_data = response.json()
                                
                                if response_data.get('content') and len(response_data['content']) > 0:
                                    ai_message = response_data['content'][0]['text']
                                else:
                                    ai_message = "I'm sorry, I couldn't generate a response. Please try again."
                                
                                st.session_state.chat_history_402.append({
                                    'role': 'assistant',
                                    'content': ai_message
                                })
                                st.rerun()
                            else:
                                st.error(f"❌ API Error: {response.status_code}")
                                st.code(response.text)
                        
                        except requests.exceptions.Timeout:
                            st.error("❌ Request timed out. Please try again.")
                        except requests.exceptions.RequestException as e:
                            st.error(f"❌ Network error: {str(e)}")
                        except Exception as e:
                            st.error(f"❌ Error calling API: {str(e)}")
                
                except KeyError:
                    st.error("⚠️ API key not found. Please add your Anthropic API key to Streamlit secrets.")
                    st.info("Add this to `.streamlit/secrets.toml`:")
                    st.code('ANTHROPIC_API_KEY = "your-key-here"')
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p style='color: #FFFFFF; font-weight: 500;'>💡 Suggested Questions:</p>", unsafe_allow_html=True)
        
        suggestions = [
            "What's the difference between job costing and process costing?",
            "How do I calculate equivalent units using the FIFO method?",
            "Explain the reciprocal method of cost allocation",
            "What is the difference between variable and fixed costs?",
            "Walk me through the 5-step production cost report"
        ]
        
        cols = st.columns(2)
        for idx, suggestion in enumerate(suggestions):
            with cols[idx % 2]:
                if st.button(f"📌 {suggestion}", key=f"suggest_{idx}"):
                    st.session_state.chat_history_402.append({
                        'role': 'user',
                        'content': suggestion
                    })
                    st.session_state.trigger_ai_call = True
                    st.rerun()
    
    with tab2:
        st.markdown("""
            <div style='
                background: linear-gradient(145deg, #1A1A2E, #151525);
                padding: 25px;
                border-radius: 15px;
                border: 1px solid #2D2D4A;
                margin-bottom: 30px;
            '>
                <h3 style='color: #FFFFFF; margin-bottom: 10px;'>📚 Key Formulas & Concepts</h3>
                <p style='color: #AAAAAA; margin: 0;'>Quick reference for essential managerial accounting formulas</p>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📐 Contribution Margin", expanded=True):
            st.markdown("**Formula:** `Contribution Margin = Sales - Variable Costs`")
            st.markdown("*Amount available to cover fixed costs and profit*")
            st.code("Example: $100,000 - $60,000 = $40,000", language=None)
        
        with st.expander("📐 Contribution Margin Ratio"):
            st.markdown("**Formula:** `CM Ratio = Contribution Margin / Sales`")
            st.markdown("*Percentage of each sales dollar available for fixed costs*")
            st.code("Example: $40,000 / $100,000 = 40%", language=None)
        
        with st.expander("📐 Break-Even Point (Units)"):
            st.markdown("**Formula:** `BEP (Units) = Fixed Costs / CM per Unit`")
            st.markdown("*Number of units needed to cover all costs*")
            st.code("Example: $30,000 / $15 = 2,000 units", language=None)
        
        with st.expander("📐 Break-Even Point (Dollars)"):
            st.markdown("**Formula:** `BEP ($) = Fixed Costs / CM Ratio`")
            st.markdown("*Sales dollars needed to break even*")
            st.code("Example: $30,000 / 0.40 = $75,000", language=None)
        
        with st.expander("📐 Predetermined Overhead Rate"):
            st.markdown("**Formula:** `Rate = Estimated Overhead / Estimated Activity`")
            st.markdown("*Used to apply overhead to jobs*")
            st.code("Example: $100,000 / 20,000 hours = $5/hour", language=None)
        
        with st.expander("📐 Equivalent Units (Weighted-Average)"):
            st.markdown("**Formula:** `EU = Units Completed + (Ending WIP × % Complete)`")
            st.markdown("*Measures work done in a period*")
            st.code("Example: 44,000 + (6,000 × 50%) = 47,000 EU", language=None)
        
        with st.expander("📐 Cost of Goods Manufactured"):
            st.markdown("**Formula:** `COGM = Beg. WIP + Manufacturing Costs - Ending WIP`")
            st.markdown("*Total cost of units completed in production*")
        
        with st.expander("📐 Prime Costs vs Conversion Costs"):
            st.markdown("**Prime Costs:** `Direct Materials + Direct Labor`")
            st.markdown("**Conversion Costs:** `Direct Labor + Factory Overhead`")
            st.markdown("*Prime costs are direct inputs; conversion costs transform materials into finished goods*")

# --- PAGE 6: ACC 405 TAX ACCOUNTING ---
elif page == "📗 ACC 405 - Tax Accounting":
    # Scroll to top
    st.components.v1.html(
        """
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
        """,
        height=0
    )
    
    st.markdown("""
        <div class='page-header'>
            <h1>📗 ACC 405 - Tax Accounting</h1>
            <p>AI-powered study assistant with full textbook access</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Home", key="back_405"):
        st.session_state.selected_page = "🏠 Home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🤖 AI Tutor", "📚 Key Concepts"])
    
    with tab1:
        st.markdown("""
            <div style='
                background: linear-gradient(145deg, #1B5E20, #0D3D12);
                padding: 25px;
                border-radius: 15px;
                border: 1px solid #2E7D32;
                margin-bottom: 30px;
            '>
                <h3 style='color: #FFFFFF; margin-bottom: 10px;'>🤖 Your ACC 405 AI Study Assistant</h3>
                <p style='color: #AAAAAA; margin: 0;'>This AI tutor has <strong style='color: #81C784;'>word-for-word access</strong> to your full tax accounting textbook. Ask anything!</p>
            </div>
        """, unsafe_allow_html=True)
        
        if 'trigger_ai_call_405' not in st.session_state:
            st.session_state.trigger_ai_call_405 = False
        
        st.markdown("<p style='color: #FFFFFF; font-weight: 500; margin-bottom: 15px;'>📖 Quick Topics:</p>", unsafe_allow_html=True)
        topic_cols = st.columns(5)
        topics_405 = [
            ("Filing Status", "Explain the different filing statuses and when to use each one"),
            ("Deductions", "What is the difference between standard and itemized deductions?"),
            ("Credits", "Explain the major tax credits available to individuals"),
            ("Income", "What types of income are taxable vs non-taxable?"),
            ("Capital Gains", "Explain how capital gains and losses are taxed")
        ]
        for idx, (label, question) in enumerate(topics_405):
            with topic_cols[idx]:
                if st.button(label, key=f"topic_405_{idx}", use_container_width=True):
                    st.session_state.chat_history_405.append({
                        'role': 'user',
                        'content': question
                    })
                    st.session_state.trigger_ai_call_405 = True
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("⚙️ AI Settings"):
            model_choice_405 = st.radio(
                "Model (Haiku is faster & cheaper, Sonnet is smarter):",
                ["claude-sonnet-4-20250514", "claude-haiku-3-5-20241022"],
                index=0,
                horizontal=True,
                key="model_405"
            )
            st.caption("💡 Tip: Use Haiku for simple questions, Sonnet for complex explanations")
        
        if st.session_state.chat_history_405:
            for message in st.session_state.chat_history_405:
                if message['role'] == 'user':
                    st.markdown(f"""
                    <div class="user-message">
                        <strong>🧑‍🎓 You:</strong><br>{message['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="ai-message">
                        <strong>🤖 AI Tutor:</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(message['content'])
            st.markdown("<br>", unsafe_allow_html=True)
        
        if 'waiting_for_response_405' not in st.session_state:
            st.session_state.waiting_for_response_405 = False
        
        with st.form(key="question_form_405", clear_on_submit=True):
            user_question_405 = st.text_area(
                "Ask your question:", 
                height=100,
                placeholder="Example: How do I calculate adjusted gross income?",
                disabled=st.session_state.waiting_for_response_405,
                key="question_input_405"
            )
            
            col1, col2 = st.columns([1, 5])
            with col1:
                submit_button_405 = st.form_submit_button(
                    "Send" if not st.session_state.waiting_for_response_405 else "Thinking...", 
                    type="primary",
                    disabled=st.session_state.waiting_for_response_405
                )
        
        btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 3])
        
        with btn_col1:
            if st.button("🗑️ Clear Chat", key="clear_chat_405"):
                st.session_state.chat_history_405 = []
                st.success("Chat cleared!")
                st.rerun()
        
        with btn_col2:
            if st.session_state.chat_history_405:
                chat_export_405 = "\n\n".join([
                    f"{'You' if m['role'] == 'user' else 'AI Tutor'}: {m['content']}" 
                    for m in st.session_state.chat_history_405
                ])
                st.download_button(
                    "📥 Export Chat",
                    chat_export_405,
                    file_name="acc405_study_session.txt",
                    mime="text/plain",
                    key="export_405"
                )
        
        should_call_api_405 = False
        
        if submit_button_405 and user_question_405.strip():
            st.session_state.chat_history_405.append({
                'role': 'user',
                'content': user_question_405
            })
            should_call_api_405 = True
        
        if st.session_state.trigger_ai_call_405:
            should_call_api_405 = True
            st.session_state.trigger_ai_call_405 = False
        
        if should_call_api_405 and st.session_state.chat_history_405:
            if st.session_state.chat_history_405[-1]['role'] == 'user':
                try:
                    api_key = st.secrets["ANTHROPIC_API_KEY"]
                    
                    system_prompt_405 = f"""You are the Tax Accounting Master Tutor, a specialized AI expert designed to help a student master federal tax accounting material.

Your goal is to provide clear, accurate, and exam-focused guidance based strictly on the textbook data provided below.

CORE RESPONSIBILITIES:
1. Knowledge Retrieval: Use the provided textbook content as your primary source of truth
2. Concept Simplification: Use the Feynman Technique - explain simply, then provide practical examples
3. Problem Solving: For tax calculations, walk through solutions step-by-step
4. Exam Prep: Create practice questions when asked

FORMATTING GUIDELINES:
- Use clear formatting for tax calculations and examples
- Use bolding for key terms
- Use bullet points for lists of requirements or qualifications
- Use tables for tax brackets, phase-outs, and comparisons
- Be professional, encouraging, and academically rigorous

INTERACTION PROTOCOLS:
- If the student is confused, ask clarifying questions
- Check their work and point out errors
- Always cite which chapter/section you're referencing
- Reference current tax law and note any recent changes

{FULL_TAX_TEXTBOOK_CONTENT}

Now answer the student's question based on this textbook content."""
                    
                    with st.spinner("🤔 Thinking..."):
                        headers = {
                            "Content-Type": "application/json",
                            "x-api-key": api_key,
                            "anthropic-version": "2023-06-01"
                        }
                        
                        api_messages_405 = []
                        for msg in st.session_state.chat_history_405:
                            api_messages_405.append({
                                "role": msg['role'],
                                "content": msg['content']
                            })
                        
                        data = {
                            "model": model_choice_405,
                            "max_tokens": 4096,
                            "system": system_prompt_405,
                            "messages": api_messages_405
                        }
                        
                        try:
                            response = requests.post(
                                "https://api.anthropic.com/v1/messages",
                                headers=headers,
                                json=data,
                                timeout=60
                            )
                            
                            if response.status_code == 200:
                                response_data = response.json()
                                
                                if response_data.get('content') and len(response_data['content']) > 0:
                                    ai_message = response_data['content'][0]['text']
                                else:
                                    ai_message = "I'm sorry, I couldn't generate a response. Please try again."
                                
                                st.session_state.chat_history_405.append({
                                    'role': 'assistant',
                                    'content': ai_message
                                })
                                st.rerun()
                            else:
                                st.error(f"❌ API Error: {response.status_code}")
                                st.code(response.text)
                        
                        except requests.exceptions.Timeout:
                            st.error("❌ Request timed out. Please try again.")
                        except requests.exceptions.RequestException as e:
                            st.error(f"❌ Network error: {str(e)}")
                        except Exception as e:
                            st.error(f"❌ Error calling API: {str(e)}")
                
                except KeyError:
                    st.error("⚠️ API key not found. Please add your Anthropic API key to Streamlit secrets.")
                    st.info("Add this to `.streamlit/secrets.toml`:")
                    st.code('ANTHROPIC_API_KEY = "your-key-here"')
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p style='color: #FFFFFF; font-weight: 500;'>💡 Suggested Questions:</p>", unsafe_allow_html=True)
        
        suggestions_405 = [
            "What is the difference between a tax deduction and a tax credit?",
            "How do I determine my filing status?",
            "What expenses can be itemized on Schedule A?",
            "Explain the rules for qualifying dependents",
            "How are long-term capital gains taxed differently than ordinary income?"
        ]
        
        cols = st.columns(2)
        for idx, suggestion in enumerate(suggestions_405):
            with cols[idx % 2]:
                if st.button(f"📌 {suggestion}", key=f"suggest_405_{idx}"):
                    st.session_state.chat_history_405.append({
                        'role': 'user',
                        'content': suggestion
                    })
                    st.session_state.trigger_ai_call_405 = True
                    st.rerun()
    
    with tab2:
        st.markdown("""
            <div style='
                background: linear-gradient(145deg, #1A1A2E, #151525);
                padding: 25px;
                border-radius: 15px;
                border: 1px solid #2D2D4A;
                margin-bottom: 30px;
            '>
                <h3 style='color: #FFFFFF; margin-bottom: 10px;'>📚 Key Tax Concepts & Formulas</h3>
                <p style='color: #AAAAAA; margin: 0;'>Quick reference for essential tax accounting concepts</p>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📐 Tax Formula (Individual)", expanded=True):
            st.markdown("**Formula:**")
            st.code("""Gross Income
- Adjustments (Above-the-Line Deductions)
= Adjusted Gross Income (AGI)
- Standard Deduction OR Itemized Deductions
- Qualified Business Income Deduction (if applicable)
= Taxable Income
× Tax Rate(s)
= Tax Liability
- Tax Credits
+ Other Taxes (Self-Employment, etc.)
= Total Tax
- Payments & Withholdings
= Tax Due or Refund""", language=None)
        
        with st.expander("📐 Adjusted Gross Income (AGI)"):
            st.markdown("**Formula:** `AGI = Gross Income - Above-the-Line Deductions`")
            st.markdown("*Above-the-line deductions include: Student loan interest, IRA contributions, HSA contributions, Self-employment tax (50%), Alimony paid (pre-2019 agreements)*")
        
        with st.expander("📐 Standard Deduction (2024)"):
            st.markdown("**Amounts:**")
            st.code("""Single: $14,600
Married Filing Jointly: $29,200
Married Filing Separately: $14,600
Head of Household: $21,900
Additional for 65+ or Blind: $1,550 (married) / $1,950 (single)""", language=None)
        
        with st.expander("📐 Capital Gains Tax Rates (2024)"):
            st.markdown("**Long-Term Capital Gains (held > 1 year):**")
            st.code("""0% Rate: Up to $47,025 (Single) / $94,050 (MFJ)
15% Rate: $47,026 - $518,900 (Single) / $94,051 - $583,750 (MFJ)
20% Rate: Above $518,900 (Single) / Above $583,750 (MFJ)""", language=None)
            st.markdown("*Short-term capital gains (held ≤ 1 year) are taxed as ordinary income*")
        
        with st.expander("📐 Filing Status Requirements"):
            st.markdown("""
**Single:** Unmarried, legally separated, or divorced on Dec 31

**Married Filing Jointly (MFJ):** Married on Dec 31, both spouses report all income

**Married Filing Separately (MFS):** Married but file separate returns

**Head of Household (HoH):** Unmarried + paid >50% of household costs + qualifying person lived with you >6 months

**Qualifying Surviving Spouse:** Spouse died in prior 2 years + dependent child + paid >50% of household costs
            """)
        
        with st.expander("📐 Dependency Tests"):
            st.markdown("""
**Qualifying Child (must meet ALL):**
1. Relationship test (child, sibling, or descendant)
2. Age test (under 19, or under 24 if full-time student, or permanently disabled)
3. Residency test (lived with taxpayer >6 months)
4. Support test (child did not provide >50% of own support)
5. Joint return test (child did not file joint return)

**Qualifying Relative (must meet ALL):**
1. Not a qualifying child of anyone
2. Relationship OR member of household test
3. Gross income test (< $5,050 in 2024)
4. Support test (taxpayer provided >50% of support)
            """)
        
        with st.expander("📐 Common Tax Credits"):
            st.markdown("""
**Child Tax Credit:** Up to $2,000 per qualifying child under 17

**Earned Income Tax Credit (EITC):** Refundable credit for low-to-moderate income workers

**American Opportunity Credit:** Up to $2,500 per student for first 4 years of college (40% refundable)

**Lifetime Learning Credit:** Up to $2,000 per return for education expenses

**Child and Dependent Care Credit:** 20-35% of up to $3,000 expenses (1 child) or $6,000 (2+ children)

**Saver's Credit:** Up to $1,000 ($2,000 MFJ) for retirement contributions
            """)
        
        with st.expander("📐 Self-Employment Tax"):
            st.markdown("**Formula:** `SE Tax = Net SE Income × 92.35% × 15.3%`")
            st.markdown("""
*Components:*
- Social Security: 12.4% (on first $168,600 in 2024)
- Medicare: 2.9% (no limit)
- Additional Medicare: 0.9% (on income > $200,000 single / $250,000 MFJ)

*Note: 50% of SE tax is deductible as an above-the-line deduction*
            """)
